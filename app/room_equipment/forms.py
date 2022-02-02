

from django.forms.models import model_to_dict
import json
# from django.forms import ModelForm
import django.forms as forms
import room_equipment.models

class ContainerDetailForm(forms.ModelForm):
    
    class Meta:
        model = room_equipment.models.Container
        fields = ['name','description','container_type_fk']


    def __init__(self,*args,**kwargs):
        super(ContainerDetailForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = \
                "shadow-sm form-control"

class ContainerItemDetailForm(forms.ModelForm):
    
    class Meta:
        model = room_equipment.models.ContainerItem
        fields = ['description']


    def __init__(self,*args,**kwargs):
        super(ContainerItemDetailForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = \
                "shadow-sm form-control"