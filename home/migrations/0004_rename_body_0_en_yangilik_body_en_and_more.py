# Generated by Django 5.0.3 on 2024-05-30 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_videomaruzalar_fakultet_id_delete_fakultet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yangilik',
            old_name='body_0_en',
            new_name='body_en',
        ),
        migrations.RenameField(
            model_name='yangilik',
            old_name='body_0_ru',
            new_name='body_ru',
        ),
        migrations.RenameField(
            model_name='yangilik',
            old_name='body_0_uz',
            new_name='body_uz',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_1_en',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_1_ru',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_1_uz',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_2_en',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_2_ru',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_2_uz',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_3_en',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_3_ru',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_3_uz',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_4_en',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_4_ru',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_4_uz',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_5_en',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_5_ru',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_5_uz',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_6_en',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_6_ru',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_6_uz',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_7_en',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_7_ru',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_7_uz',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_8_en',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_8_ru',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_8_uz',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_9_en',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_9_ru',
        ),
        migrations.RemoveField(
            model_name='yangilik',
            name='body_9_uz',
        ),
        migrations.AddField(
            model_name='elon',
            name='fayl_1',
            field=models.FileField(blank=True, upload_to='elon_fayl/'),
        ),
        migrations.AddField(
            model_name='elon',
            name='fayl_2',
            field=models.FileField(blank=True, upload_to='elon_fayl/'),
        ),
        migrations.AddField(
            model_name='elon',
            name='fayl_3',
            field=models.FileField(blank=True, upload_to='elon_fayl/'),
        ),
        migrations.AddField(
            model_name='elon',
            name='fayl_4',
            field=models.FileField(blank=True, upload_to='elon_fayl/'),
        ),
        migrations.AddField(
            model_name='elon',
            name='fayl_5',
            field=models.FileField(blank=True, upload_to='elon_fayl/'),
        ),
        migrations.AddField(
            model_name='yangilik',
            name='fayl_1',
            field=models.FileField(blank=True, upload_to='yangilik_fayl/'),
        ),
        migrations.AddField(
            model_name='yangilik',
            name='fayl_2',
            field=models.FileField(blank=True, upload_to='yangilik_fayl/'),
        ),
        migrations.AddField(
            model_name='yangilik',
            name='fayl_3',
            field=models.FileField(blank=True, upload_to='yangilik_fayl/'),
        ),
        migrations.AddField(
            model_name='yangilik',
            name='fayl_4',
            field=models.FileField(blank=True, upload_to='yangilik_fayl/'),
        ),
        migrations.AddField(
            model_name='yangilik',
            name='fayl_5',
            field=models.FileField(blank=True, upload_to='yangilik_fayl/'),
        ),
    ]
