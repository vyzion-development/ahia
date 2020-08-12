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
from django.conf.urls.static import static
# importing from views 👇🏿
from ahia import views as asset_views


urlpatterns = [
    path('accounts/', include( 'registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
    path('asset/add/', asset_views.add_asset, name='add_assets'),
    path('',asset_views.index, name = 'list_assets'),
    path('asset/<int:pk>/delete/', asset_views.delete_asset, name='delete_assets'),
    path('asset/<int:pk>/edit/', asset_views.edit_asset, name='edit_assets'),
    path('', include('blog.urls')),

    #path('asset/list/', asset_views.list_assets, name='list_assets')


    path('profile/add/', asset_views.add_profile, name='add_profile'),
    path('',asset_views.index, name = 'list_assets'),
    path('asset/<int:pk>/delete/', asset_views.delete_asset,name='delete_assets'),
    path('asset/<int:pk>/edit/',asset_views.edit_asset,name='edit_assets'),
    path('asset/<int:pk>/profile/', asset_views.profile, name='user_profile'),
    #path('asset/list/', asset_views.list_assets, name='list_assets')
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

