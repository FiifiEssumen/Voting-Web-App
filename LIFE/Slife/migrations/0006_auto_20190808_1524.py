# Generated by Django 2.2.1 on 2019-08-08 15:24

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Slife', '0005_auto_20190808_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='option'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set(),
        ),
    ]
