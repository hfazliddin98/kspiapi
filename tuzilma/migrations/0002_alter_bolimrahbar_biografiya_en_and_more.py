# Generated by Django 5.0.3 on 2024-05-30 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuzilma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bolimrahbar',
            name='biografiya_en',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='bolimrahbar',
            name='biografiya_ru',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='bolimrahbar',
            name='biografiya_uz',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='fakultetrahbar',
            name='biografiya_en',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='fakultetrahbar',
            name='biografiya_ru',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='fakultetrahbar',
            name='biografiya_uz',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='kafedrarahbar',
            name='biografiya_en',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='kafedrarahbar',
            name='biografiya_ru',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='kafedrarahbar',
            name='biografiya_uz',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='markazrahbar',
            name='biografiya_en',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='markazrahbar',
            name='biografiya_ru',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='markazrahbar',
            name='biografiya_uz',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='rektoratrahbar',
            name='biografiya_en',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='rektoratrahbar',
            name='biografiya_ru',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='rektoratrahbar',
            name='biografiya_uz',
            field=models.TextField(blank=True),
        ),
    ]
