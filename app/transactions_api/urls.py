from django.conf.urls import url
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.urlpatterns import format_suffix_patterns
from transactions_api import views

schema_view = get_schema_view(
   openapi.Info(
      title="Transactions API",
      default_version='v1',
      description="View transactions users",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="admin@client-site.com"),
      license=openapi.License(name="Your License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('users/', views.UsersList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
