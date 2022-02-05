from django.urls import path, include, re_path



import core.views
import stock.views
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View


app_name = 'stock'

urlpatterns = [
    re_path(r"^itemloc/search/$", stock.views.SearchItemLocationView.as_view(), name="Search_items"),
    re_path(r"^getitems/$", stock.views.GetItems.as_view(), name="GetItems"),
]

