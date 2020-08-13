from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Asset, Profile
from .forms import Asset_info_Form, ProfileForm
from django.conf import settings


def index(request):
    assets = Asset.objects.all()
    return render(request, "assets/list_assets.html", context= {"assets": assets})




def profile(request, pk):
    profile = get_object_or_404(Profile, user_id=pk)
    assets = Asset.objects.filter()
    return render(request,"assets/user_profile.html", context= {"profile": profile})

def add_profile(request):
    if request.method == 'GET':
       form = ProfileForm() 
    else:
       form = ProfileForm(data=request.POST)
       if form.is_valid():
           form.save(commit=False)
           return redirect(to='user_profile', pk=request.user.pk)
    return render(request, "assets/add_profile.html", {"form": form})

def add_asset(request):
    if request.method == 'GET':
       form = Asset_info_Form() 
    else:
       form = Asset_info_Form(data=request.POST)
       if form.is_valid():
           form.save()
           return redirect(to='list_assets')   #may need to change home
           
    return render(request, "assets/add_assets.html", {"form": form})


def delete_asset(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        asset.delete()
        return redirect(to='list_assets')

    return render(request, "assets/delete_assets.html",
                 {"asset": asset})

def edit_asset(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'GET':
        form = Asset_info_Form(instance=asset)
    else:
        form = Asset_info_Form(data=request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect(to='list_assets')   

    return render(request, "assets/edit_assets.html", {
      "form": form,
      "asset": asset
       })                      

