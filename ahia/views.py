from django.contrib.auth.decorators import login_required
from django.shortcuts import render 
from .models import Asset
from django.shortcuts import render, redirect, get_object_or_404
from .forms import asset_info_Form

# Create your views here.
@login_required
def index(request):
    assets = Asset.objects.all()
    return render(request, 'assets/list_assets.html', context={'assets': assets})

def add_assets(request):
    if request.method == 'GET':
        form = asset_info_Form()
    else:
        form = asset_info_Form(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_assets')

    return render(request, "assets/add_assets.html", {"form": form})

def delete_assets(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        asset.delete()
        return redirect(to='list_assets')
    return render(request, "assets/delete_assets.html",
                  {"assets": asset})