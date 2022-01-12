from django.urls import path
from . import views


app_name = 'hotel'

urlpatterns = [
    # path('store/', views.store, name = "store"),
    path('store/', views.IndexView.as_view(), name = "store"),
]
