from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse
from core.models import DefaultObject
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError, FieldError
import room_equipment.models
from django.utils.html import mark_safe

class Manufacturer(DefaultObject, models.Model):

    """
    Item Manufacturer
    """

    logo = models.ImageField(
        _("logo"), 
        upload_to='uploads/logo/manufacturer', 
        height_field=None, 
        width_field=None, 
        max_length=None,
        blank=True
        )


    class Meta:
        verbose_name = _("Manufacturer")
        verbose_name_plural = _("Manufacturers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Manufacturer_detail", kwargs={"pk": self.pk})

    def logo_tag(self):
        if self.logo:
            return mark_safe('<img src="%s" width="50px" height="50px" />'%(self.logo.url))
        return None
    logo_tag.short_description = 'Manufacturer logo'
    logo_tag.allow_tags = True

class Item(DefaultObject, models.Model):
    """
    Item
    """
    manufacturer_fk = models.ForeignKey(
        Manufacturer, verbose_name=_("manufacturer"), on_delete=models.CASCADE,
        null=True)
    model = models.CharField(_("model"), max_length=50, blank=True)
    is_consumable = models.BooleanField(_("is_consumable"),default=False)
    icon = models.ImageField(
        _("icon"), 
        upload_to='uploads/icons/item', 
        height_field=None, 
        width_field=None, 
        max_length=None,
        blank=True
        )

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Item_detail", kwargs={"pk": self.pk})
    def icon_tag(self):
        if self.icon:
            return mark_safe('<img src="%s" width="50px" height="50px" />'%(self.icon.url))
        return None
    icon_tag.short_description = 'Item icon'
    icon_tag.allow_tags = True

class ItemLocation(models.Model):
    """
    Lokalizacja itemu
    """
    description = models.TextField(_("description"),blank=True)
    container_item_fk = models.ForeignKey(
        room_equipment.models.ContainerItem, 
        verbose_name=_("container_item"), 
        on_delete=models.CASCADE, null=True
        )
    item_fk = models.ForeignKey(Item, verbose_name=_("item"), on_delete=models.CASCADE)
    serial = models.CharField(_("serial"), max_length=50,blank=True)
    pieces = models.IntegerField(_("pieces"))
    mac = models.CharField(_("mac"), max_length=50,blank=True)
    ip = models.CharField(_("ip"), max_length=50,blank=True)


    class Meta:
        verbose_name = _("ItemLocation")
        verbose_name_plural = _("ItemLocations")

    def get_info(self):
        return f"{self.item_fk.name} x{self.pieces}"

    def __str__(self):
        return self.get_info()

    def get_absolute_url(self):
        return reverse("ItemLocation_detail", kwargs={"pk": self.pk})