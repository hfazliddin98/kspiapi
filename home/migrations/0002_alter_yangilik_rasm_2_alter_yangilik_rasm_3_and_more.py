# Generated by Django 5.0.3 on 2024-03-29 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yangilik',
            name='rasm_2',
            field=models.ImageField(blank=True, upload_to='yangilik/'),
        ),
        migrations.AlterField(
            model_name='yangilik',
            name='rasm_3',
            field=models.ImageField(blank=True, upload_to='yangilik/'),
        ),
        migrations.AlterField(
            model_name='yangilik',
            name='rasm_4',
            field=models.ImageField(blank=True, upload_to='yangilik/'),
        ),
        migrations.AlterField(
            model_name='yangilik',
            name='rasm_5',
            field=models.ImageField(blank=True, upload_to='yangilik/'),
        ),
    ]