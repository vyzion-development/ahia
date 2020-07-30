from .models import Asset
from django import forms

class asset_info_Form(forms.ModelForm):
    class Meta:
        model = Asset
        fields = [
            'asset_title',
            'asset_type',         
            'asset_upload',
            'asset_category',
        ]
