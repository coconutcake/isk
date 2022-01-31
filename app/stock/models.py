from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse
from core.models import DefaultObject
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError, FieldError
import room_equipment.models

class Item(DefaultObject, models.Model):
    """
    Item
    """
    serial = models.CharField(_("serial"), max_length=70, blank=True)

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Item_detail", kwargs={"pk": self.pk})


class ItemLocation(models.Model):
    """
    Lokalizacja itemu
    """
    description = models.TextField(_("description"),blank=True)
    container_item_fk = models.ForeignKey(room_equipment.models.ContainerItem, verbose_name=_("container_item"), on_delete=models.CASCADE)
    item_fk = models.ForeignKey(Item, verbose_name=_("item"), on_delete=models.CASCADE)
    pieces = models.IntegerField(_("pieces"))
    class Meta:
        verbose_name = _("ItemLocation")
        verbose_name_plural = _("ItemLocations")

    def get_info(self):
        return f"{self.item_fk.name} x{self.pieces}"

    def __str__(self):
        return self.get_info()


    def get_absolute_url(self):
        return reverse("ItemLocation_detail", kwargs={"pk": self.pk})