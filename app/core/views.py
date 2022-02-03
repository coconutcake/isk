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

class WelcomeView(View):


    template_name = "core/welcome.html"
    

    def get(self, request, *args, **kwargs):

        return render(
            request, 
            self.template_name, 
            self.get_context(request)
            )
    

    def get_context(self, request):
        """
        Context zwracany do GET
        """
        
        lan_ip = fnc.get_ip_lan()
        server_type = fnc.get_server_type()
        platform = fnc.get_platform_info()
        get_wan = fnc.get_wan()
        get_db = fnc.get_db()
        pip_packages = fnc.get_pip_packages()

        context = {
            "get_wan": get_wan,
            "get_ip_lan": lan_ip,
            "get_db": get_db,
            "get_server_type": server_type,
            "get_platform_info": platform,
            "get_pip_packages": pip_packages

        }


        return context


class DashboardView(View):
    """
    Menu
    """

    pick_form = core.forms.PickForm
    stow_form = ""
    transfer_form = ""
    template_name = "core/dashboard.html"

    def get_querydict_data(self,request,data_key=None,*args,**kwargs):
        """
        Zwraca QueryDict z request.POST[data_key]
        """

        data = request.POST

        for k,v in data.items():
            if k == data_key:
                data2 = json.loads(json.dumps(data.get(data_key, '')))

                return QueryDict(data2)

    def get_dict_data(self, request,data_key=None,*args,**kwargs):
        """
        Zwraca Dict z request.POST[data_key]        
        """

        data = dict(request.POST.dict())
        items = urllib.parse.parse_qs(data[data_key])
        di = {}
        for i,v in items.items():
            di[i] = v[0]
        
        return di

    def get_eval_dict(self, dictionary):
        """
        Zwraca przekonwerowany Dict z odpowiednimi typami danych
        """
        di = dictionary
        for i, v in di.items():
            try:
                di[i] = literal_eval(v)
            except ValueError:
                pass

        return di
    
    def get_context_data(self, request, **kwargs):
        context = {}
        context["pick_form"] = self.pick_form
        return context
    
    def get(self, request, pk=None, *args, **kwargs):

        return render(
            request, 
            template_name=self.template_name,
            context=self.get_context_data(request,**kwargs)
            )

    def post(self, request, pk=None, *args, **kwargs):

        #print(self.get_querydict_data(request, data_key="form_data", *args, **kwargs))
        #print(self.get_querydict_data(request, data_key="additional_data", *args, **kwargs))
        #print(self.get_dict_data(request, data_key="additional_data", *args, **kwargs))
        #print(self.get_eval_dict(self.get_dict_data(request, data_key="additional_data", *args, **kwargs)))
        
        return JsonResponse(data={"status": "OK"})


class SearchItemView(View):

    def get(self, request, pk=None, *args, **kwargs):

        queryset = stock.models.Item.objects.filter(
            Q(name__contains=request.GET.get("name",None)) & 
            Q(pk__in=request.GET.get("item",None))
        ).values()

        print(queryset)
        
        return JsonResponse(data={"params": request.GET, "query": list(queryset)})