# Generated by Django 5.0.3 on 2024-04-04 06:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_galareya_tur_id_galareya_tur_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galareya',
            name='tur_id',
        ),
        migrations.AddField(
            model_name='galareya',
            name='tur_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.galareyaturi'),
            preserve_default=False,
        ),
    ]