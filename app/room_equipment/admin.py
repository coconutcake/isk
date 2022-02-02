from django.contrib import admin
from . import models
from django.utils.translation import gettext_lazy as _


class ContainerAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'description','container_type_fk','id']
    fieldsets = (
        (_('Name'),{'fields': 
            ('name',)}),
        (_('Description'),{"fields": 
            ('description',)}),
        (_('Relations'),{"fields": 
            ('container_type_fk',)}
        )
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('name','description')
        }),
    ) 
admin.site.register(models.Container,ContainerAdmin)

class ContainerFieldLocationAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['get_name','description','field_fk','get_area','container_fk','id']
    fieldsets = (
        (_('Description'),{"fields": 
            ('description',)}),
        (_('Relations'),{"fields": 
            ('field_fk','container_fk',)}
        )
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('name','description')
        }),
    ) 
admin.site.register(models.ContainerFieldLocation,ContainerFieldLocationAdmin)

class ContainerTypeAdmin(admin.ModelAdmin):


    ordering = ['id']
    list_display = [
        'icon_tag','name', 'description','id']
    fieldsets = (
        (_('Name'),{'fields': 
            ('name',)}),
        (_('Description'),{"fields": 
            ('description','icon',)}
        )
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('name','description')
        }),
    ) 
admin.site.register(models.ContainerType,ContainerTypeAdmin)

class ContainerItemTypeAdmin(admin.ModelAdmin):


    ordering = ['id']
    list_display = ['icon_tag', 'name', 'description','id']
    fieldsets = (
        (_('Name'),{'fields': 
            ('name',)}),
        (_('Description'),{"fields": 
            ('description','icon')}
        )
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('name','description')
        }),
    ) 
admin.site.register(models.ContainerItemType,ContainerItemTypeAdmin)

class ContainerLocationAdmin(admin.ModelAdmin):


    ordering = ['id']
    readonly_fields = ('location_barcode','qrcode','qrcode_render',)
    list_display = ['location_barcode','level','position','depth','id']
    fieldsets = (
        (_('Barcode'),{'fields': 
            ('location_barcode','qrcode','qrcode_render')}),
        (_('Relations'),{'fields': 
            ('container_fk',)}),
        (_('Location'),{"fields": 
            ('level','position',)}
        )
    )
admin.site.register(models.ContainerLocation,ContainerLocationAdmin)

class ContainerItemAdmin(admin.ModelAdmin):


    ordering = ['id']
    list_display = [
        'description',
        'container_location_fk',
        'container_item_type_fk',
        'id'
        ]
    fieldsets = (
        (_('Description'),{"fields": 
            ('description',)}),
        (_('Relations'),{'fields': 
            ('container_location_fk','container_item_type_fk',)}
        )
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('description',)
        }),
    ) 
admin.site.register(models.ContainerItem,ContainerItemAdmin)


