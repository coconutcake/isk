# Generated by Django 4.0 on 2022-01-13 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_equipment', '0013_containeritemtype_containeritem'),
    ]

    operations = [
        migrations.AddField(
            model_name='containeritemtype',
            name='icon',
            field=models.ImageField(blank=True, upload_to='uploads/icons/containeritemtype', verbose_name='icon'),
        ),
        migrations.DeleteModel(
            name='ContainerItem',
        ),
    ]
