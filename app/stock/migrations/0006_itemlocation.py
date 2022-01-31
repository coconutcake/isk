# Generated by Django 4.0 on 2022-01-23 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room_equipment', '0018_delete_itemlocation'),
        ('stock', '0005_delete_itemlocation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('pieces', models.IntegerField(verbose_name='pieces')),
                ('container_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room_equipment.containeritem', verbose_name='container_item')),
                ('item_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.item', verbose_name='item')),
            ],
            options={
                'verbose_name': 'ItemLocation',
                'verbose_name_plural': 'ItemLocations',
            },
        ),
    ]