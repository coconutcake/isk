

from django.forms.models import model_to_dict
import json
# from django.forms import ModelForm
import django.forms as forms
import map.models

class FieldDetailForm(forms.ModelForm):
    
    class Meta:
        model = map.models.Field
        fields = ["level","position"]


    def __init__(self,*args,**kwargs):
        super(FieldDetailForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = \
                "shadow-sm form-control"
            self.fields['level'].widget.attrs['readonly'] = True
            self.fields['position'].widget.attrs['readonly'] = True

            # self.fields['description'].widget.attrs['rows'] = 4
            # self.fields['description'].widget.attrs['columns'] = 15


