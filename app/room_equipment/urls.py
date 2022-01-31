from django.urls import path, include, re_path



from room_equipment import views
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View


app_name = 'room_equipment'

urlpatterns = [
    re_path(r"^container/$", views.ContainerDetailView.as_view(), name="container_detail"),
    re_path(r"^container_item/$", views.ContainerItemDetailView.as_view(), name="container_item_detail"),
]

