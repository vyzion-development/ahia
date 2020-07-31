from .models import Asset
from django import forms

class Asset_info_Form(forms.ModelForm):
    class Meta:
        model = Asset
        fields = [
            'asset_type', 
            'asset_title',  
            'asset_description',
            'asset_update',      
            'asset_upload',
            'asset_want',
        ]
