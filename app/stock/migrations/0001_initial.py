# Generated by Django 4.0 on 2022-02-02 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('room_equipment', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('defaultobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.defaultobject')),
                ('model', models.CharField(blank=True, max_length=50, verbose_name='model')),
                ('is_consumable', models.BooleanField(default=False, verbose_name='is_consumable')),
                ('icon', models.ImageField(blank=True, upload_to='uploads/icons/item', verbose_name='icon')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
            bases=('core.defaultobject', models.Model),
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('defaultobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.defaultobject')),
                ('logo', models.ImageField(blank=True, upload_to='uploads/logo/manufacturer', verbose_name='logo')),
            ],
            options={
                'verbose_name': 'Manufacturer',
                'verbose_name_plural': 'Manufacturers',
            },
            bases=('core.defaultobject', models.Model),
        ),
        migrations.CreateModel(
            name='ItemLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('serial', models.CharField(blank=True, max_length=50, verbose_name='serial')),
                ('pieces', models.IntegerField(verbose_name='pieces')),
                ('mac', models.CharField(blank=True, max_length=50, verbose_name='mac')),
                ('ip', models.CharField(blank=True, max_length=50, verbose_name='ip')),
                ('container_item_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='room_equipment.containeritem', verbose_name='container_item')),
                ('item_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.item', verbose_name='item')),
            ],
            options={
                'verbose_name': 'ItemLocation',
                'verbose_name_plural': 'ItemLocations',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='manufacturer_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.manufacturer', verbose_name='manufacturer'),
        ),
    ]
