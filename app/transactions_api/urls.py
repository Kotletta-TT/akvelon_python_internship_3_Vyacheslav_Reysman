
from django.urls import path
from transactions_api import views


urlpatterns = [
    # path('users/', views.UsersList.as_view()),
    path('user/me/', views.UserDetail.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('transaction/<int:pk>/', views.TransactDetail.as_view()),
]
