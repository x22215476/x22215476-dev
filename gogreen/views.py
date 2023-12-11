# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Plants, Order
from .forms import PlantsForm, PurchaseForm
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User 

@login_required(login_url='/signin/')
def index(request):
    best_selling = Plants.objects.order_by('-cost')[:15]
    
    context = {'best_selling': best_selling}
    return render(request, 'gogreen/index.html', context)

@login_required(login_url='/signin/')
def show(request, plant_id):
    try:
        plant = Plants.objects.get(id=plant_id)
    except Plants.DoesNotExist:
        raise Http404("Plant does not exist")
    return render(request, 'Plants/show.html', {'plant': plant})

@login_required(login_url='/signin/')
def create_listing(request):
    if request.method == 'POST':
        form = PlantsForm(request.POST)
        if form.is_valid():
            plant = form.save(commit=False)
            plant.seller = request.user
            plant.save()
            return redirect('gogreen:plant_list')  
    else:
        form = PlantsForm()

    return render(request, 'gogreen/create_listing.html', {'form': form})

@login_required(login_url='/signin/')
def plant_list(request):
    plants = Plants.objects.all()
    return render(request, 'gogreen/plant_list.html', {'plants': plants})
    
@login_required(login_url='/signin/')
def purchase_plant(request, plant_id):
    plant = get_object_or_404(Plants, id=plant_id)

    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            total_cost = plant.cost * quantity

            # Create an Order for the user
            order = Order.objects.create(user=request.user, total_cost=total_cost)
            order.plants.add(plant)

            return redirect('gogreen:order_history')  # Update this to the URL name of your order history view
    else:
        form = PurchaseForm()

    return render(request, 'gogreen/purchase_plant.html', {'plant': plant, 'form': form})

    
@login_required(login_url='/signin/')
def update_plant(request, plant_id):
    plant = get_object_or_404(Plants, pk=plant_id)

    if request.method == 'POST':
        form = PlantsForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('gogreen:plant_list')
    else:
        form = PlantsForm(instance=plant)

    return render(request, 'gogreen/update_plant.html', {'form': form, 'plant': plant})
    
def order_table(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    print(order.plants.all())  # Add this line for debugging
    return render(request, 'gogreen/order_table.html', {'order': order})
    
@login_required(login_url='/signin/')
def delete_plant(request, plant_id):
    plant = get_object_or_404(Plants, pk=plant_id)

    if request.method == 'POST':
        plant.delete()
        return redirect('gogreen:plant_list')  # Redirect to the plant list after deletion

    return render(request, 'gogreen/delete_plant.html', {'plant': plant})
    
@login_required(login_url='/signin/')
def delete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    if request.method == 'POST':
        order.delete()
        return redirect('gogreen:index')  # Redirect to the home page after deleting the order

    return render(request, 'gogreen/delete_order.html', {'order': order})

@login_required(login_url='/signin/')
def thank_you(request):
    return render(request, 'gogreen/thank_you.html')

class PurchasePlantView(View):
    template_name = 'gogreen/purchase_plant.html'

    def get(self, request, plant_id):
        # Retrieve the plant object
        plant = get_object_or_404(Plants, id=plant_id)

        # Create a new PurchaseForm instance
        form = PurchaseForm()

        # Render the purchase plant form with the plant details and the form
        return render(request, self.template_name, {'plant': plant, 'form': form})

    def post(self, request, plant_id):
        # Retrieve the plant object
        plant = get_object_or_404(Plants, id=plant_id)

        # Process the form submission
        form = PurchaseForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            total_cost = plant.cost * quantity

            # Create an Order for the user
            order = Order.objects.create(user=request.user, total_cost=total_cost)
            order.save()

            # Redirect to the thank-you page with the order_id
            return redirect('gogreen:thank_you', order_id=order.id)

        # If the form is not valid, render the purchase plant form with errors
        return render(request, self.template_name, {'plant': plant, 'form': form})
