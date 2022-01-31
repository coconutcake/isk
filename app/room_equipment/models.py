from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse
from core.models import DefaultObject
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError, FieldError
from django.utils.html import mark_safe
import map.models
from map.models import Field

class ContainerType(DefaultObject, models.Model):

    """
    ContainerType
    """

    icon = models.ImageField(
        _("icon"), 
        upload_to='uploads/icons/container', 
        height_field=None, 
        width_field=None, 
        max_length=None,
        blank=True
        )

    class Meta:
        verbose_name = _("Containertype")
        verbose_name_plural = _("Containertypes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Containertype_detail", kwargs={"pk": self.pk})

    def icon_tag(self):
        if self.icon:
            return mark_safe('<img src="%s" width="50px" height="50px" />'%(self.icon.url))
        return None
    icon_tag.short_description = 'icon'
    icon_tag.allow_tags = True





class Container(DefaultObject, models.Model):

    """
    Container (szafka, paleta, dzwi ... )
    """

    container_type_fk = models.ForeignKey(
        ContainerType, verbose_name=_("container_type"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Container")
        verbose_name_plural = _("Containers")

    def __str__(self):
        return self.name

    def get_fields__str__(self):
        return f"{', '.join(list(self.fields.all().values_list('name',flat=True)))}"


    def get_absolute_url(self):
        return reverse("Container_detail", kwargs={"pk": self.pk})


class ContainerLocation(models.Model):

    description = models.TextField(_("description"),blank=True)
    field_fk = models.ForeignKey(Field, verbose_name=_("field"), on_delete=models.CASCADE)
    container_fk = models.ForeignKey(Container, verbose_name=_("container"), on_delete=models.CASCADE)
    class Meta:
        verbose_name = _("ContainerLocation")
        verbose_name_plural = _("ContainerLocations")

    def __str__(self):
        return f"{self.container_fk} > {self.field_fk.name}"


    def get_name(self):
        return f"{self.container_fk} > {self.field_fk.name}"

    def get_area(self):
        return f"{self.field_fk.area_fk}"

    def get_absolute_url(self):
        return reverse("ContainerLocation_detail", kwargs={"pk": self.pk})




class ContainerItemType(DefaultObject, models.Model):

    """
    Tot, karton, pojemnik
    """

    icon = models.ImageField(
        _("icon"), 
        upload_to='uploads/icons/containeritemtype', 
        height_field=None, 
        width_field=None, 
        max_length=None,
        blank=True)

    class Meta:
        verbose_name = _("ContainerItemType")
        verbose_name_plural = _("ContainerItemTypes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ContainerItemType_detail", kwargs={"pk": self.pk})
        
    def icon_tag(self):
        if self.icon:
            return mark_safe('<img src="%s" width="50px" height="50px" />'%(self.icon.url))
        return None
    icon_tag.short_description = 'icon'
    icon_tag.allow_tags = True



class ContainerItem(DefaultObject, models.Model):

    """
    Elementy kontenera
    """

    container_fk = models.ForeignKey(
        Container, verbose_name=_("container"), on_delete=models.CASCADE)
    container_item_type_fk = models.ForeignKey(
        ContainerItemType, verbose_name=_("container_item_type"), 
        on_delete=models.CASCADE)
    position = models.IntegerField(_("position"))
    level = models.IntegerField(_("level"), default=0)
    depth = models.IntegerField(_("depth"), default=0)

    

    class Meta:
        verbose_name = _("ContainerItem")
        verbose_name_plural = _("ContainerItems")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ContainerItem_detail", kwargs={"pk": self.pk})



