from django.contrib import admin

# Register your models here.
from . import models
from django.utils.translation import gettext_lazy as _


class ItemAdmin(admin.ModelAdmin):
    ordering = ['id']
    readonly_fields = ('icon_tag',)
    list_display = ['name','manufacturer_fk','model','description','is_consumable','id']
    fieldsets = (
        (_('Name'),{'fields': 
            ('name','manufacturer_fk','model','icon','icon_tag',)}),
        (_('Description'),{"fields": 
            ('description','is_consumable',)}
        )
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('name','description')
        }),
    ) 
admin.site.register(models.Item,ItemAdmin)

class ItemLocationAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['get_item_name','serial','pieces','description','id']
    fieldsets = (
        (_('Description'),{"fields": 
            ('description','serial','mac','ip',)}),
        (_('Relations'),{"fields": 
            ('item_fk','container_item_fk',)}),
        (_('Quantity'),{"fields": 
            ('pieces',)}
        )
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('description')
        }),
    ) 

    @admin.display(empty_value='None')
    def get_item_name(self, obj):
        return obj.item_fk.name
admin.site.register(models.ItemLocation,ItemLocationAdmin)

class ManufacturerAdmin(admin.ModelAdmin):
    ordering = ['id']
    readonly_fields = ('logo_tag',)
    list_display = ['name','description','id']
    fieldsets = (
        (_('Name'),{'fields': 
            ('name','logo','logo_tag',)}),
        (_('Description'),{"fields": 
            ('description',)}
        )
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('name','description')
        }),
    ) 
admin.site.register(models.Manufacturer,ManufacturerAdmin)