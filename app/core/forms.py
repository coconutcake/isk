from unicodedata import name
from django.forms.models import model_to_dict
import json
from django.forms import ModelChoiceField, ModelForm
import django.forms as forms
from django.core.exceptions import ValidationError, FieldError
import map.models
import room_equipment.models
import stock.models


class PickForm(forms.Form):
    """
    Pick form
    """
    
    item_queryset = stock.models.Item.objects.all()
    area_queryset = map.models.Area.objects.all()

    item = forms.ModelChoiceField(queryset=item_queryset, empty_label="(Nothing)")
    name = forms.CharField(label="name", max_length=50, required=False)
    serial = forms.CharField(label="serial", max_length=70, required=False)
    area = forms.ModelChoiceField(queryset=area_queryset, empty_label="(Nothing)")

