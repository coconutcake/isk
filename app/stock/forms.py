from unicodedata import name
from django.forms.models import model_to_dict
import json
from django.forms import ModelChoiceField, ModelForm
import django.forms as forms
from django.core.exceptions import ValidationError, FieldError
import map.models
import room_equipment.models
import stock.models


class ItemLocationForm(forms.ModelForm):
    
    class Meta:
        model = stock.models.ItemLocation
        fields = "__all__"