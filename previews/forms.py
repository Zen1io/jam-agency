# forms.py
from django import forms
from .models import BillboardPreview

class BillboardPreviewForm(forms.ModelForm):
    class Meta:
        model = BillboardPreview
        fields = ['uploaded_design']
