# Generated by Django 5.0.3 on 2024-06-07 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuzilma', '0006_rektoratrahbar_rektorat_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bolimhodim',
            name='bolim_boshligi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fakultethodim',
            name='bolim_boshligi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='kafedrahodim',
            name='bolim_boshligi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='markazhodim',
            name='bolim_boshligi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rektorathodim',
            name='bolim_boshligi',
            field=models.BooleanField(default=False),
        ),
    ]
