# Generated by Django 4.0 on 2022-01-13 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('room_equipment', '0010_alter_containertype_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitContainer',
            fields=[
                ('defaultobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.defaultobject')),
                ('icon', models.ImageField(blank=True, upload_to='uploads/icons/unitcontainer', verbose_name='icon')),
            ],
            options={
                'verbose_name': 'UnitContainer',
                'verbose_name_plural': 'UnitContainers',
            },
            bases=('core.defaultobject', models.Model),
        ),
    ]
