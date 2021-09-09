
from django.urls import path
from transactions_api import views


urlpatterns = [
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('transaction/<int:pk>/', views.TransactDetail.as_view()),
]
