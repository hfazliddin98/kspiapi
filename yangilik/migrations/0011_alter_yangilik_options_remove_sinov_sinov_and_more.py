# Generated by Django 5.0.3 on 2024-03-23 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yangilik', '0010_alter_sinov_sinov'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='yangilik',
            options={},
        ),
        migrations.RemoveField(
            model_name='sinov',
            name='sinov',
        ),
        migrations.AlterField(
            model_name='sinov',
            name='yangilik',
            field=models.ManyToManyField(related_name='sinovs', to='yangilik.yangilik'),
        ),
    ]