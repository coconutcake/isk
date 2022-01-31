# Generated by Django 4.0 on 2022-01-14 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_remove_field_x_remove_field_y_field_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='field',
            name='level',
        ),
        migrations.RemoveField(
            model_name='field',
            name='position',
        ),
        migrations.AddField(
            model_name='field',
            name='x',
            field=models.IntegerField(null=True, verbose_name='x'),
        ),
        migrations.AddField(
            model_name='field',
            name='y',
            field=models.IntegerField(null=True, verbose_name='y'),
        ),
    ]