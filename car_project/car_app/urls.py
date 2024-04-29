
from . import views
from django.urls import path
from .views import move_car
from .views import update_positions

urlpatterns = [
    path('list_cars/', views.list_cars, name='list_cars'),
    path('update_positions/', update_positions, name='update_positions'),
    path('update_car_order/<int:car_id>/<int:new_position>/', views.update_positions, name='update_car_order'),
    path('query_cars/<str:color>/', views.query_cars, name='query_cars'),
    # Add the following line for the /cars/ path
    path('', views.list_cars, name='list_cars_default'),
    path('move_car/<int:car_id>/<int:new_position>/', move_car, name='move_car'),
]
