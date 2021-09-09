
from django.urls import path
from transactions_api import views


urlpatterns = [
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('transaction/id/<int:pk>/', views.TransactId.as_view()),
    path('transactions/', views.TransactList.as_view())
]
