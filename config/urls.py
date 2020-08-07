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
from django.conf import settings
from django.urls import include, path
# importing album from views 👇🏿
from ahia import views as asset_views


urlpatterns = [
    path('',asset_views.index, name='home'),
    path('asset/add/', asset_views.add_assets,
     name='add_assets'),
    path('asset/<int:pk>/delete/',asset_views.delete_assets,
    name = 'delete_assets'),
    path('asset/profile/', asset_views.profile, name='user_profile'),
]