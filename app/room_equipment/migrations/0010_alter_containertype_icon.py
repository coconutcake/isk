# Generated by Django 4.0 on 2022-01-13 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_equipment', '0009_containertype_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='containertype',
            name='icon',
            field=models.ImageField(blank=True, upload_to='uploads/icons/container', verbose_name='icon'),
        ),
    ]