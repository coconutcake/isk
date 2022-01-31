from django.contrib import admin
from . import models
from django.utils.translation import gettext_lazy as _


# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'description','id']
    fieldsets = (
        (_('Name'),{'fields': 
            ('name',)}),
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

admin.site.register(models.Department,DepartmentAdmin)

class MapAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'description','department_fk','floor','id']
    fieldsets = (

        (_('Name'),{'fields': 
            ('name',)}),
        (_('Description'),{"fields": 
            ('description','floor',)}),
        (_('Relations'),{"fields": 
            ('department_fk',)})
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('name','description')
        }),
    ) 

admin.site.register(models.Map,MapAdmin)

class AreaAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'description', 'map_fk', 'id']
    fieldsets = (

        (_('Name'),{'fields': 
            ('name',)}),
        (_('Description'),{"fields": 
            ('description',)}),
        (_('Relations'),{"fields": 
            ('map_fk',)})
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('name','description')
        }),
    ) 

admin.site.register(models.Area,AreaAdmin)

class FieldAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'description', 'level','position','area_fk','id']
    fieldsets = (

        (_('Name'),{'fields': 
            ('name',)}),
        (_('Description'),{"fields": 
            ('description',)}),
        (_('Position'),{'fields': 
            ('level','position',)}),
        (_('Relations'),{"fields": 
            ('area_fk',)})
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('name','description')
        }),
    ) 

admin.site.register(models.Field,FieldAdmin)