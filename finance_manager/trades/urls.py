from django.urls import path
from . import views

urlpatterns = [
    path('trades/', views.trade_list),
    path('trades/<int:pk>/', views.trade_detail),
]