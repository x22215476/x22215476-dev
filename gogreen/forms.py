# forms.py
from django import forms
from .models import Plants

class PlantsForm(forms.ModelForm):
    class Meta:
        model = Plants
        fields = ['name', 'botanical_name', 'cost']

class PurchaseForm(forms.Form):
    quantity = forms.IntegerField()
    
class UpdatePlantsForm(forms.ModelForm):
    class Meta:
        model = Plants
        fields = ['name', 'botanical_name', 'cost']