# Generated by Django 4.2.11 on 2024-10-28 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_efirname_efir'),
    ]

    operations = [
        migrations.AddField(
            model_name='elon',
            name='xalqaro',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='yangilik',
            name='xalqaro',
            field=models.BooleanField(default=False),
        ),
    ]
