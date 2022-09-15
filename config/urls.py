
from django.contrib import admin
from django.urls import path, include
from app.views import index, add_info
from app.views import *
from .urls_yasg import urlpatterns_yasg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth', include('djoser.urls')),
    path('api/v1/auth-token', include('djoser.urls.authtoken')),
    path('', add_info, name='add_info'),
    path('', index),
    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('api/v1/client/create/', ClientCreateView.as_view()),
    path('api/v1/client/list/', ClientListView.as_view()),
    path('api/v1/client/detail/<int:pk>', ClientDetailView.as_view()),
] + urlpatterns_yasg
