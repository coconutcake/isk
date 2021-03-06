from django.urls import path, include, re_path



from core import views
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View
from rest_framework.schemas import get_schema_view

app_name = 'core'

urlpatterns = [

    re_path(r"^dash/$", views.DashboardView.as_view(), name="Dashboard"),
    re_path(r"^stow/$", views.StowView.as_view(), name="Stow"),
    re_path(r"^stow-create-form/$", views.StowCreateForm.as_view(), name="StowCreateForm"),
    

]

