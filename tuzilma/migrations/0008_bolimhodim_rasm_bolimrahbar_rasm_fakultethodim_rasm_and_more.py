# Generated by Django 5.0.3 on 2024-06-07 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuzilma', '0007_bolimhodim_bolim_boshligi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bolimhodim',
            name='rasm',
            field=models.ImageField(default=1, upload_to='rahbarlar/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bolimrahbar',
            name='rasm',
            field=models.ImageField(default=1, upload_to='rahbarlar/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fakultethodim',
            name='rasm',
            field=models.ImageField(default=1, upload_to='rahbarlar/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fakultetrahbar',
            name='rasm',
            field=models.ImageField(default=1, upload_to='rahbarlar/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kafedrahodim',
            name='rasm',
            field=models.ImageField(default=1, upload_to='rahbarlar/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kafedrarahbar',
            name='rasm',
            field=models.ImageField(default=1, upload_to='rahbarlar/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='markazhodim',
            name='rasm',
            field=models.ImageField(default=1, upload_to='rahbarlar/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='markazrahbar',
            name='rasm',
            field=models.ImageField(default=1, upload_to='rahbarlar/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rektorathodim',
            name='rasm',
            field=models.ImageField(default=1, upload_to='rahbarlar/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rektoratrahbar',
            name='rasm',
            field=models.ImageField(default=1, upload_to='rahbarlar/'),
            preserve_default=False,
        ),
    ]