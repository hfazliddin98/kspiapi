# Generated by Django 5.0.3 on 2024-03-25 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yangilik', '0017_remove_yangilik_body_0_remove_yangilik_body_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='yangilik',
            name='til',
            field=models.ManyToManyField(to='yangilik.til'),
        ),
    ]