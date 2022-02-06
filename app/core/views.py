from webbrowser import get
from django.shortcuts import render
import json
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
import datetime
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
from rest_framework import status
import stock.forms
from django.template.loader import render_to_string
from rest_framework import status

class DashboardView(View):
    """
    Menu
    """

    template_name = "core/dashboard.html"
    
    def get_context_data(self, request, **kwargs):
        context = {}
        # context["pick_form"] = self.pick_form
        return context
    
    def get(self, request, pk=None, *args, **kwargs):

        return render(
            request, 
            template_name=self.template_name,
            context=self.get_context_data(request,**kwargs)
            )

    def post(self, request, pk=None, *args, **kwargs):

        #print(fnc.get_querydict_data(request, data_key="form_data", *args, **kwargs))
        #print(fnc.get_querydict_data(request, data_key="additional_data", *args, **kwargs))
        #print(fnc.get_dict_data(request, data_key="additional_data", *args, **kwargs))
        #print(fnc.get_eval_dict(self.get_dict_data(request, data_key="additional_data", *args, **kwargs)))
        
        return JsonResponse(data={"status": status.HTTP_202_NOT_FOUND})

class StowView(View):
    """
    Stow
    """

    template_name = "core/stow.html"


    def get_context_data(self, request, **kwargs):
        context = {}
        return context
    
    def get(self, request, pk=None, *args, **kwargs):

        return render(
            request, 
            template_name=self.template_name,
            context=self.get_context_data(request,**kwargs)
            )
 
class StowCreateForm(View):
    """
    Stow
    """

    form = stock.forms.ItemLocationForm
    form_template = "core/forms/stow-form.html"


    def get_context_data(self, request, **kwargs):
        context = {}
        context["form"] = self.form
        return context
    
    def get(self, request, pk=None, *args, **kwargs):

        return render(
            request, 
            template_name=self.form_template,
            context=self.get_context_data(request,**kwargs)
            )

    def post(self, request, pk=None, *args, **kwargs):

        json_data = fnc.get_json_data(request, data_key="form_data", *args, **kwargs)
        json_additional_data = fnc.get_json_data(request, data_key="additional_data", *args, **kwargs)
        
        form_data = fnc.get_form_querydict_data(
            request,
            data_key="form_data", #< - {"data": JSON.Stringify($data)}
            )

        form = self.form(data=form_data)

        if form.is_valid():
            form.save()
            return JsonResponse(
                data={
                    "status":status.HTTP_201_CREATED,
                    "status_html": "<span><i class='fas fa-check text-success'></i> created!</span>"
                    }
                )
        else:
            form_string_html = render_to_string(self.form_template, {'form': form}, request=request)
            return JsonResponse(
                data={
                    "status":status.HTTP_400_BAD_REQUEST, 
                    "status_html": "<span><i class='fas fa-exclamation-circle text-danger'></i> Failed to create!</span>",
                    "form_string_html":form_string_html,
                    }
                )
class SearchItemView(View):

    def get(self, request, pk=None, *args, **kwargs):

        queryset = stock.models.Item.objects.filter(
            Q(name__contains=request.GET.get("name",None)) & 
            Q(pk__in=request.GET.get("item",None))
        ).values()

        print(queryset)
        
        return JsonResponse(data={"params": request.GET, "query": list(queryset)})