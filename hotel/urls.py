from django.urls import path
from . import views



app_name = 'hotel'

urlpatterns = [
    # path('store/', views.store, name = "store"),
    path('house/', views.HouseView.as_view(), name = "house"),
    path('room_list/', views.RoomsView.as_view(), name = "room_list"),
]
