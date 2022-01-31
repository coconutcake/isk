# Generated by Django 4.0 on 2022-01-23 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0007_remove_field_container_fk'),
        ('room_equipment', '0018_delete_itemlocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='fields',
            field=models.ManyToManyField(to='map.Field', verbose_name='fields'),
        ),
    ]