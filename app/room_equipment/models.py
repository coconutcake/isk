
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
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
import qrcode
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.core.files import File
from PIL import Image, ImageDraw
from django.utils.html import escape
from django.utils.html import mark_safe
from django.core.exceptions import ObjectDoesNotExist

# Validators
def validate_container_fk(value):
    """
    Validates if ContainerFieldLocation is set
    """
    container = Container.objects.get(pk=value)
    try:
        obj = ContainerFieldLocation.objects.get(container_fk=value)
    except ObjectDoesNotExist:
        raise ValidationError(
            "No ContainerFieldLocation assosiation found! Please assosiate Container in table ContainerFieldLocation in order to get required data from Foreign keys!"
        )



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

class ContainerFieldLocation(models.Model):

    description = models.TextField(_("description"),blank=True)
    field_fk = models.ForeignKey(
        Field, verbose_name=_("field"), on_delete=models.CASCADE)
    container_fk = models.ForeignKey(
        Container, verbose_name=_("container"), on_delete=models.CASCADE)
    class Meta:
        verbose_name = _("ContainerFieldLocation")
        verbose_name_plural = _("ContainerFieldLocations")

    def __str__(self):
        return f"{self.container_fk} > {self.field_fk.name}"

    def get_name(self):
        return f"{self.container_fk} > {self.field_fk.name}"

    def get_area(self):
        return f"{self.field_fk.area_fk}"

    def get_absolute_url(self):
        return reverse("ContainerLocation_detail", kwargs={"pk": self.pk})



class ContainerLocation(models.Model):
    """
    Container Location (lokalizacje kontenera)
    """
    container_fk = models.ForeignKey(
        Container, verbose_name=_("container"), 
        validators=[validate_container_fk],
        on_delete=models.CASCADE)
    level = models.IntegerField(_("level"))
    position = models.IntegerField(_("position"))
    depth = models.IntegerField(_("depth"), default=0)
    location_barcode = models.CharField(_("location_barcode"), max_length=70,blank=True)
    qrcode = models.ImageField(
        _("qrcode"), 
        upload_to='uploads/barcodes/containerlocations', 
        height_field=None, 
        width_field=None, 
        max_length=None,
        blank=True
        )

    class Meta:
        verbose_name = _("containerlocation")
        verbose_name_plural = _("containerlocations")





    def get_barcode_string(self):
        """
        Generate barcode
        """

        model_container_field_location = ContainerFieldLocation
        
        instance_container_field_location = \
            model_container_field_location.objects.filter(
                container_fk=self.container_fk
                ).first()


        level = self.level
        position = self.position
        container = self.container_fk

        warning_not_containerfieldset = "ContainerFieldLocation not set!"

        try:
            area = instance_container_field_location.field_fk.area_fk.name
        except:
            area = False
        try:   
            map = instance_container_field_location.field_fk.area_fk.map_fk.name
        except:
            map = False
        try:
            dept = instance_container_field_location.field_fk.area_fk.map_fk.department_fk.name
        except:
            dept = False
        
        if any([area,map,dept]):
            barcode = f"{dept}-{map}-{area}-{container}-{level}{position}"
            return barcode.replace(" ","")
        else :
            barcode = warning_not_containerfieldset
            return barcode
        

    def save_qrcode(self):
        """
        Save barcode qr to imagefield qrcode
        """
        
        barcode = self.get_barcode_string()

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=12,
            border=2,
        )

        qr.add_data(barcode)
        qr.make(fit=True)

        filename = f"{barcode}.png"
        img = qr.make_image()
        canvas = Image.new('RGB', (350,350), 'white')
        canvas.paste(img)
        buffer = io.BytesIO()
        canvas.save(buffer,'PNG')
        self.qrcode.save(filename,File(buffer),save=False)
        canvas.close()

    def save_qrcode(self):
        """
        Save barcode qr to imagefield qrcode
        """
        
        barcode = self.get_barcode_string()

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=12,
            border=2,
        )

        qr.add_data(barcode)
        qr.make(fit=True)

        filename = f"{barcode}.png"
        img = qr.make_image()
        canvas = Image.new('RGB', (350,350), 'white')
        canvas.paste(img)
        buffer = io.BytesIO()
        canvas.save(buffer,'PNG')



        self.qrcode.save(filename,File(buffer),save=False)
        canvas.close()

    def get_qrcode(self, barcode):
        """
        Save barcode qr to imagefield qrcode
        """

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=12,
            border=2,
        )

        qr.add_data(barcode)
        qr.make(fit=True)

        filename = f"{barcode}.png"
        img = qr.make_image()
        canvas = Image.new('RGB', (350,350), 'white')
        canvas.paste(img)
        buffer = io.BytesIO()
        canvas.save(buffer,'PNG')

        canvas.close()

        return filename, File(buffer)

    def __str__(self):
        return f"{self.location_barcode}"

    def get_absolute_url(self):
        return reverse("containerlocation_detail", kwargs={"pk": self.pk})

    def qrcode_render(self):
        return mark_safe(f"<img src='{self.qrcode.url}' />")

    qrcode_render.short_description = 'QR'
    qrcode_render.allow_tags = True

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
        blank=True
        )

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

class ContainerItem(models.Model):

    """
    Container location items
    """
    description = models.TextField(_("description"),blank=True)
    container_location_fk = models.ForeignKey(
        ContainerLocation, verbose_name=_("container_location"), 
        on_delete=models.CASCADE,null=True, 
        help_text="This indicates location in container")
    container_item_type_fk = models.ForeignKey(
        ContainerItemType, verbose_name=_("container_item_type"), 
        on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("ContainerItem")
        verbose_name_plural = _("ContainerItems")

    def get_container_location_info(self):
        return f"{self.container_location_fk.location_barcode} - {self.container_item_type_fk}"

    def __str__(self):
        return self.get_container_location_info()

    def get_absolute_url(self):
        return reverse("ContainerItem_detail", kwargs={"pk": self.pk})


@receiver(post_save, sender=ContainerLocation)
def create_barcode(sender, instance, created, **kwargs):

    if not created:
        objs = sender.objects.filter(pk=instance.pk)
        objs.update(
            level = instance.level,
            position = instance.position,
            location_barcode = instance.get_barcode_string(),
            container_fk = instance.container_fk
        )        
    else:
        instance.location_barcode = instance.get_barcode_string()
        instance.save_qrcode()
        instance.save()


    

