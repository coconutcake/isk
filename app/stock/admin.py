from django.contrib import admin

# Register your models here.
from . import models
from django.utils.translation import gettext_lazy as _


class ItemAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'description','serial','id']
    fieldsets = (
        (_('Name'),{'fields': 
            ('name',)}),
        (_('Description'),{"fields": 
            ('description','serial',)}
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
    list_display = ['get_item_name','pieces','description','id']
    fieldsets = (
        (_('Description'),{"fields": 
            ('description',)}),
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