from django.urls import path
from . import views
from .views import index, show, create_listing, plant_list, purchase_plant, update_plant, delete_plant, thank_you

app_name = 'gogreen'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:plant_id>/', views.show, name='show'),
    path('create_listing/', views.create_listing, name='create_listing'),
    path('plant_list/', views.plant_list, name='plant_list'),
    path('purchase_plant/<int:plant_id>/', views.purchase_plant, name='purchase_plant'),
    path('update_plant/<int:plant_id>/', update_plant, name='update_plant'),
    #path('order_table/', order_table, name='order_table'),
    path('delete_plant/<int:plant_id>/', delete_plant, name='delete_plant'),
    #path('order_confirmation/<int:order_id>/', OrderConfirmationView.as_view(), name='order_confirmation'),
    #path('delete_order/<int:order_id>/', delete_order, name='delete_order'),
    path('purchase/', purchase_plant, name='purchase_plant'),
    path('thank-you/', thank_you, name='thank_you'),
]
