from django.urls import path, include, re_path



from map import views
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View


app_name = 'map'

urlpatterns = [
    re_path(r"^area/$", views.AreaView.as_view(), name="Area"),
    re_path(r"^area/field/$", views.FieldDetailView.as_view(), name="field_detail"),
]

