# Generated by Django 4.2.11 on 2024-08-21 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abiturient', '0007_baxomezoni_kvota'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtishBallari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=255)),
                ('name_ru', models.CharField(blank=True, max_length=255)),
                ('name_en', models.CharField(blank=True, max_length=255)),
                ('fayl', models.FileField(blank=True, upload_to='otishballari')),
            ],
        ),
    ]