# Generated by Django 5.0.3 on 2024-06-01 08:16

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abiturient', '0003_bakalavr_magistr_qabulhujjati_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakalavr',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='callmarkaz',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='magistr',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='qabulhujjati',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
