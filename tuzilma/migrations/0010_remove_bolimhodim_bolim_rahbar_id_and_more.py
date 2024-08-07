# Generated by Django 5.0.3 on 2024-06-20 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuzilma', '0009_remove_kafedrahodim_kafedra_rahbar_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bolimhodim',
            name='bolim_rahbar_id',
        ),
        migrations.RemoveField(
            model_name='fakultethodim',
            name='fakultet_rahbar_id',
        ),
        migrations.RemoveField(
            model_name='markazhodim',
            name='markaz_rahbar_id',
        ),
        migrations.AddField(
            model_name='bolimhodim',
            name='bolim_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tuzilma.bolim'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fakultethodim',
            name='fakultet_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tuzilma.fakultet'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='markazhodim',
            name='markaz_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tuzilma.markaz'),
            preserve_default=False,
        ),
    ]
