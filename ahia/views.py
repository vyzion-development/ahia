from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Asset 
from .forms import Asset_info_Form


def index(request):
    assets = Asset.objects.all()
    return render(request, "assets/list_assets.html", context= {"assets": assets})

def add_assets(request):
    if request.method == 'GET':
       form = Asset_info_Form() 
    else:
       form = Asset_info_Form(data=request.POST)
       if form.is_valid():
           form.save()
           return redirect(to='home')   #may need to change home
           
    return render(request, "assets/add_assets.html", {"form": form})


def delete_assets(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        asset.delete()
        return redirect(to='home')

    return render(request, "asset/delete_assets.html",
                 {"asset": asset})

