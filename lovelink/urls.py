from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, re_path, include

urlpatterns = [
    path('', lambda request: redirect('admin/', permanent=True)),
    path('admin/', admin.site.urls),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
]
