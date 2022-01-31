# Generated by Django 4.0 on 2022-01-08 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('room_equipment', '0001_initial'),
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='container_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room_equipment.container', verbose_name='container'),
        ),
        migrations.AddField(
            model_name='area',
            name='map_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.map', verbose_name='map'),
        ),
    ]