# Generated by Django 5.0.3 on 2024-06-21 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Akademik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(blank=True, max_length=255)),
                ('title_ru', models.CharField(blank=True, max_length=255)),
                ('title_en', models.CharField(blank=True, max_length=255)),
                ('body_uz', models.TextField(blank=True)),
                ('body_ru', models.TextField(blank=True)),
                ('body_en', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ilmiy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(blank=True, max_length=255)),
                ('title_ru', models.CharField(blank=True, max_length=255)),
                ('title_en', models.CharField(blank=True, max_length=255)),
                ('body_uz', models.TextField(blank=True)),
                ('body_ru', models.TextField(blank=True)),
                ('body_en', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jamoatchilik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(blank=True, max_length=255)),
                ('title_ru', models.CharField(blank=True, max_length=255)),
                ('title_en', models.CharField(blank=True, max_length=255)),
                ('body_uz', models.TextField(blank=True)),
                ('body_ru', models.TextField(blank=True)),
                ('body_en', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Madaniy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(blank=True, max_length=255)),
                ('title_ru', models.CharField(blank=True, max_length=255)),
                ('title_en', models.CharField(blank=True, max_length=255)),
                ('body_uz', models.TextField(blank=True)),
                ('body_ru', models.TextField(blank=True)),
                ('body_en', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Oquv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(blank=True, max_length=255)),
                ('title_ru', models.CharField(blank=True, max_length=255)),
                ('title_en', models.CharField(blank=True, max_length=255)),
                ('body_uz', models.TextField(blank=True)),
                ('body_ru', models.TextField(blank=True)),
                ('body_en', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Yoshlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(blank=True, max_length=255)),
                ('title_ru', models.CharField(blank=True, max_length=255)),
                ('title_en', models.CharField(blank=True, max_length=255)),
                ('body_uz', models.TextField(blank=True)),
                ('body_ru', models.TextField(blank=True)),
                ('body_en', models.TextField(blank=True)),
            ],
        ),
    ]