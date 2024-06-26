# Generated by Django 4.2.11 on 2024-06-29 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abiturient', '0006_rename_bakalavr_abiturientbakalavr_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaxoMezoni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(blank=True, max_length=255)),
                ('title_ru', models.CharField(blank=True, max_length=255)),
                ('title_en', models.CharField(blank=True, max_length=255)),
                ('fayl', models.FileField(blank=True, upload_to='mezon')),
            ],
        ),
        migrations.CreateModel(
            name='Kvota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=255)),
                ('name_ru', models.CharField(blank=True, max_length=255)),
                ('name_en', models.CharField(blank=True, max_length=255)),
                ('fayl', models.FileField(blank=True, upload_to='mezon')),
            ],
        ),
    ]
