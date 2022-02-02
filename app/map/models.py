
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse
from core.models import DefaultObject
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError, FieldError


class Department(DefaultObject, models.Model):

    """
    Department
    """

    class Meta:
        verbose_name = _("department")
        verbose_name_plural = _("departments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("department_detail", kwargs={"pk": self.pk})

class Map(DefaultObject, models.Model):
    
    """
    Map
    """

    department_fk = models.ForeignKey(
        Department, verbose_name=_("department"), on_delete=models.CASCADE)
    floor = models.IntegerField(_("floor"),blank=False)

    class Meta:
        verbose_name = _("map")
        verbose_name_plural = _("maps")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("map_detail", kwargs={"pk": self.pk})

class Area(DefaultObject, models.Model):

    """
    Area
    """

    map_fk = models.ForeignKey(
        Map, verbose_name=_("map"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("area")
        verbose_name_plural = _("areas")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("area_detail", kwargs={"pk": self.pk})

class Field(DefaultObject, models.Model):

    """
    Field
    """

    level = models.IntegerField(_("level"),null=True)
    position = models.IntegerField(_("position"),null=True)
    area_fk = models.ForeignKey(
        Area, verbose_name=_("area"), on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("Field")
        verbose_name_plural = _("Fields")

   

    def __str__(self):
        return f"{self.name} > {self.area_fk.name}"

    def get_absolute_url(self):
        return reverse("Field_detail", kwargs={"pk": self.pk})
