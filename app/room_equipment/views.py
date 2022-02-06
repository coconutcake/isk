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



# Create your views here.
class ContainerDetailView(View):
    """ 
    
    """
    template_detail_form = "room_equipment/forms/container_detail_form.html"
    detail_form = room_equipment.forms.ContainerDetailForm
    container_item_model = room_equipment.models.ContainerItem
    container_item_detail_form = room_equipment.forms.ContainerItemDetailForm
    model = room_equipment.models.Container


    def get(self, request, pk=None, *args, **kwargs):


        pk = self.request.GET.get('pk')
        container_instance = self.model.objects.get(pk=pk)
        items_of_container = self.container_item_model.objects.filter(container_fk=container_instance) if container_instance else []
        
        print(container_instance)

        form_instances = []
        for instance in items_of_container:
            form_instances.append(self.container_item_detail_form(instance=instance))

        if request.method == "GET":
            if pk:
                return render(
                    request,
                    self.template_detail_form,
                    {
                        "detail_form":self.detail_form(instance=container_instance),
                        "container_item_detail_forms":form_instances
                    }
                )
        
        return render(
            request,
            self.template_detail_form,
            {
                "detail_form":self.detail_form(instance=container_instance),
                "container_item_detail_forms":form_instances
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




class ContainerItemDetailView(View):
    """ 
    
    """
    template_detail_form = "room_equipment/forms/container_item_detail_form.html"
    detail_form = room_equipment.forms.ContainerItemDetailForm
    model = room_equipment.models.ContainerItem

    def prepare_form_data(self,request,data_key=None,*args,**kwargs):

        data = request.POST

        for k,v in data.items():
            if k == data_key:
                data2 = json.loads(json.dumps(data.get(data_key, '')))

                return QueryDict(data2)

    def get_object(self, *args, **kwargs):

        obj = get_object_or_404(self.model, pk=self.kwargs['pk'])

        return obj

    def get(self, request, pk=None, *args, **kwargs):


        pk = self.request.GET.get('pk')
        instance = self.model.objects.get(pk=pk)
        
        
        if request.method == "GET":
            if pk:
                return render(
                    request,
                    self.template_detail_form,
                    {
                        "detail_form":self.detail_form(instance=instance)
                    }
                )
        
        return render(
            request,
            self.template_detail_form,
            {
                "detail_form":self.detail_form(instance=instance)
            }
        )

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


