# Generated by Django 2.2.1 on 2019-08-19 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Slife', '0008_auto_20190819_1238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': (('can vote only once ', 'can view vote'),)},
        ),
    ]
