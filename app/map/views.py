from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from django.http import QueryDict
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404
import map.models
import room_equipment.models
import room_equipment.forms
import stock.models
# Create your views here.
import map.forms
from func import functions as fnc
from django.db.models import Q




class AreaView(View):

    """
    Map
    """

    template_name = "map/area.html"

    def get(self, request, *args, **kwargs):

        return render(
            request, 
            self.template_name, 
            self.get_context(request, *args, **kwargs)
            )
    

    def get_context(self, request, *args, **kwargs):


        area_pk = self.request.GET.get('pk')
        area = map.models.Area.objects.get(pk=area_pk)
        area_fields = map.models.Field.objects.filter(area_fk_id=area_pk)

        rows = list(map.models.Field.objects.filter(area_fk_id=area_pk).values_list('level', flat=True).distinct())
        columns = list(map.models.Field.objects.filter(area_fk_id=area_pk).values_list('position', flat=True).distinct())

        matrix = []

        for row in rows:
            dirow = {}
            dirow['row'] = row
            dirow['columns'] = []
            for column in columns:
                dico = {}
                dico['level'] = row
                dico['position'] = column
                dico['field'] = None
                for field in area_fields:
                    if field.level == dico['level'] and field.position == dico['position']:
                        dico['field'] = field
                dirow['columns'].append(dico)
            matrix.append(dirow)



        context = {
            "get_area_fields": area_fields,
            "rows":rows,
            "columns": columns,
            "matrix": matrix,
            "area": area
        }

        print(area_fields)

        return context





class FieldDetailView(View):
    """ 
    
    """
    template_detail_form = "map/forms/field_detail_form.html"
    detail_form = map.forms.FieldDetailForm
    model = map.models.Field



    def get(self, request, pk=None, *args, **kwargs):


        field_pk = self.request.GET.get('pk',None)
        field_name = self.request.GET.get('name','')

        field_instances =  map.models.Field.objects.filter(Q(pk=field_pk)|Q(name__contains=field_name))
        print(field_instances)

        form_instances = []
        for instance in field_instances:
            form_instances.append(self.detail_form(instance=instance))

        print(form_instances)

        if request.method == "GET":
            if field_pk:
                return render(
                    request,
                    self.template_detail_form,
                    {

                        "detail_forms":form_instances
                    }
                )
        
        return render(
            request,
            self.template_detail_form,
            {

                "detail_forms":form_instances
            }
        )

    def prepare_form_data(self,request,data_key=None,*args,**kwargs):

        data = request.POST

        for k,v in data.items():
            if k == data_key:
                data2 = json.loads(json.dumps(data.get(data_key, '')))

                return QueryDict(data2)

    def get_object(self, *args, **kwargs):

        obj = get_object_or_404(self.model, pk=self.kwargs['pk'])

        return obj

    def post(self, request, *args,**kwargs):

        form_data = self.prepare_form_data(
            request,
            data_key="data", #< - {"data": JSON.Stringify($data)}
            )

        instance = self.model.objects.get(pk=self.request.GET.get('pk'))
        form = self.detail_form(data=form_data,instance=instance)

        if form.is_valid():
            form.save()
            return JsonResponse(data={"status":"OK"})
        else:
            return JsonResponse(data={"status":"Failed"})

