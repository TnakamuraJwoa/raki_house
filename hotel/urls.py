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
    path('select_create/<int:pk>/', views.SelectCreateView.as_view(), name = "select_create"),
    path('mk_calendar/', views.MkCalendarView.as_view(), name = "mk_calendar"),
    path('tree_calendar/', views.TreeCalendarView.as_view(), name = "tree_calendar"),
    path('my_page/', views.MyPageView.as_view(), name = "my_page"),
    path('reserve_syoukai/', views.ReserveReferenceConfView.as_view(), name = "reserve_syoukai"),
    path('reserve_conp/', views.ReserveConpView.as_view(), name = "reserve_conp"),
    path('reserve_cancel/', views.ReserveCancelView.as_view(), name = "reserve_cancel"),
]
