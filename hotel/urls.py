from django.urls import path
from . import views



app_name = 'hotel'

urlpatterns = [
    # path('store/', views.store, name = "store"),
    path('store/', views.StoreView.as_view(), name = "store"),
]
