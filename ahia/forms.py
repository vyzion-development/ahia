from .models import Asset
from django import forms

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = [
            'asset_type', 
            'asset_title',  
            'asset_description'      
            'asset_upload',
            'asset_category',
        ]
