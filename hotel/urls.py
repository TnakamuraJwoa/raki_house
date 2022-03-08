from django.urls import path
from . import views



app_name = 'hotel'

urlpatterns = [
    # path('store/', views.store, name = "store"),
    path('house/', views.HouseView.as_view(), name = "house"),
    path('room/<int:pk>/', views.RoomView.as_view(), name = "room"),
    path('room_list/', views.RoomsView.as_view(), name = "room_list"),
    path('reserve_confirmation/', views.ReserveConfirmationView.as_view(), name = "reserve_confirmation"),
    path('reserve_create/', views.ReserveCreateView.as_view(), name = "reserve_create"),
    path('reserve_reference_conf/', views.ReserveReferenceConfView.as_view(), name = "reserve_reference_conf"),
]
