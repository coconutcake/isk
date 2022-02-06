from cProfile import label
from django.shortcuts import render
from webbrowser import get
import json
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
import datetime
from map.models import Area
from core.models import User
from func import functions as fnc
import map.forms
import core.forms
import stock.models
from django.http import QueryDict
from django.forms.models import model_to_dict
import urllib.parse
from ast import literal_eval
from django.core import serializers
from django.db.models import Q
import room_equipment.models
from rest_framework import status

# Create your views here.



class GetItems(View):
    """
    Gets Item
    """
    def convert_query_to_json_autocomplete(self, label, value, query):
        """
        Converts query to json autocomplete field 
        """

        li = []

        for obj in query:
            o = model_to_dict(obj)
            label_ = o[label]
            value_ = o[value]
            di = {"label":label_,"value":value_}
            li.append(di)
            
        return json.dumps(li)

    def get_context_data(self, request, **kwargs):

        context = {}
        return context
    
    def get(self,request,*args,**kwargs):
        
        name = request.GET.get("name","")

        # -----> Query 
        query = stock.models.Item.objects.filter(
            Q(name__iexact=name) | Q(name__icontains=name)
        ) if name else stock.models.Item.objects.all()

        # -----> JsonResponse 
        return JsonResponse(data={
            "json":self.convert_query_to_json_autocomplete(
                label="name",
                value="id", 
                query=query
                )
        })
class GetItemLocations(View):
    """
    Gets Item
    """
    template_name = "stock/itemlocations.html"

    def get_context_data(self, request, **kwargs):

        name = request.GET.get("name","")
        id = request.GET.get("id","")

        # -----> Query LocationItems 
        item_locations = stock.models.ItemLocation.objects.filter(
            Q(item_fk__id__in=[id]) | Q(item_fk__name__icontains=name)
        ) if name else stock.models.ItemLocation.objects.all()

        # -----> Queries ?????????
        containers = room_equipment.models.Container.objects.filter(
            )
        item_locations = stock.models.ItemLocation.objects.filter(
            container_item_fk__container_fk__in=containers
            )
        container_items = room_equipment.models.ContainerItem.objects.filter(
            container_fk__in=containers
            )

        context = {}
        context['itemlocations'] = item_locations
        return context
    
    def get(self,request,*args,**kwargs):
               
        # -----> JsonResponse 
        return render(
            request, 
            template_name=self.template_name,
            context=self.get_context_data(request,**kwargs)
            )

class GetContainerItems(View):
    """
    Gets Item
    """
    def convert_query_to_json_autocomplete_strlabel(self, value, query):
        """
        Converts query to json autocomplete field 
        """

        li = []

        for obj in query:
            print(obj.__str__())
            o = model_to_dict(obj)
            label_ = obj.__str__()
            value_ = o[value]
            di = {"label":label_,"value":value_}
            li.append(di)
            
        return json.dumps(li)

    def get_context_data(self, request, **kwargs):

        context = {}
        return context
    
    def get(self,request,*args,**kwargs):
        
        name = request.GET.get("name","")

        # -----> Query 
        query = room_equipment.models.ContainerItem.objects.filter(
            Q(container_location_fk__location_barcode__iexact=name) | 
            Q(container_location_fk__location_barcode__icontains=name)
        ) if name else room_equipment.models.ContainerItem.objects.all()

        # -----> JsonResponse 
        return JsonResponse(data={
            "json":self.convert_query_to_json_autocomplete_strlabel(
                value="id", 
                query=query
                )
        })



       
class SearchItemLocationView(View):
    """
    Widok przeszukajacy po parametrach get
    """

    def get(self, request, pk=None, *args, **kwargs):

        # -----> Get params 
        item = request.GET.get("item",None)
        name = request.GET.get("name",None)
        area = request.GET.get("area",None)
        serial = request.GET.get("serial",None)

        # -----> Query if foreignkey pk in get params else get all instances 
        areas = map.models.Area.objects.filter(pk__in=[area]) if area else map.models.Area.objects.all()
        all_items = stock.models.Item.objects.filter(pk__in=[item]) if item else stock.models.Item.objects.all()
        
        area_list = []
        
        if areas:

            for area in areas:

                # -----> Queries 
                container_locations = room_equipment.models.ContainerLocation.objects.filter(field_fk__area_fk=area)
                container_locations_container_pks = list(container_locations.values_list("container_fk",flat=True).distinct())
                containers = room_equipment.models.Container.objects.filter(pk__in=container_locations_container_pks)
                item_locations = stock.models.ItemLocation.objects.filter(container_item_fk__container_fk__in=containers)
                container_items = room_equipment.models.ContainerItem.objects.filter(container_fk__in=containers)

                area_dict = model_to_dict(area)
                container_list = []

                # -----> Container loop 
                for container in containers:

                    container_dict = model_to_dict(container)
                    container_dict['container_items'] = []
                    
                    # -----> ItemLocation loop  
                    for item_location in item_locations:
                        if item_location.container_item_fk.container_fk == container:

                            # -----> ContainerItem loop 
                            for container_item in container_items:
                                if container_item == item_location.container_item_fk:
                                    
                                    container_item_dict = model_to_dict(container_item)
                                    container_item_dict['items'] = []

                                    if container_item == item_location.container_item_fk:
                                        
                                        # -----> Q object query 
                                        container_items_query = item_locations.filter(
                                            Q(item_fk__in=all_items.values_list("pk",flat=True).distinct()) & 
                                            Q(item_fk__name__contains=name) & Q(item_fk__serial__contains=serial) & 
                                            Q(container_item_fk=container_item)
                                            )

                                        container_item_dict['items'] = [model_to_dict(i) for i in container_items_query]
                                    
                                    container_dict['container_items'].append(container_item_dict)
                                    
                    container_list.append(container_dict)

                area_dict['containers'] = container_list
                area_list.append(area_dict)

        # -----> Payload 
        json_payload = {
            'area_list':area_list
        }

        return JsonResponse(data=(json_payload),safe=False)