# Generated by Django 4.0 on 2022-01-23 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0007_remove_field_container_fk'),
        ('room_equipment', '0019_container_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='area_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='map.area', verbose_name='area'),
        ),
    ]
