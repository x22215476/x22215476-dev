from django.urls import path
from . import views
from .views import index, show, purchase_plant, update_plant, delete_plant, thank_you

app_name = 'gogreen'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:plant_id>/', views.show, name='show'),
    path('create_listing/', views.create_listing, name='create_listing'),
    path('plant_list/', views.plant_list, name='plant_list'),
    path('purchase_plant/<int:plant_id>/', views.purchase_plant, name='purchase_plant'),
    path('update_plant/<int:plant_id>/', update_plant, name='update_plant'),
    path('delete_plant/<int:plant_id>/', delete_plant, name='delete_plant'),
    path('purchase/', purchase_plant, name='purchase_plant'),
    path('thank-you/', thank_you, name='thank_you'),
]
