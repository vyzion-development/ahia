"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ahia import views as assets_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', assets_views.list_assets, name='list_assets'),
    path('assets/<int:pk>/add/', assets_views.add_assets, name='add_assets'),
    path('assets/<int:pk>/delete/', assets_views.delete_assets,name='delete_assets'),
    
    ]