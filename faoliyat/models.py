from django.db import models

class Jamoatchilik(models.Model):
    title_uz = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    body_uz = models.TextField(blank=True)
    body_ru = models.TextField(blank=True)
    body_en = models.TextField(blank=True)


class Madaniy(models.Model):
    title_uz = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    body_uz = models.TextField(blank=True)
    body_ru = models.TextField(blank=True)
    body_en = models.TextField(blank=True)

    
class Oquv(models.Model):
    title_uz = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    body_uz = models.TextField(blank=True)
    body_ru = models.TextField(blank=True)
    body_en = models.TextField(blank=True)

class Akademik(models.Model):
    title_uz = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    body_uz = models.TextField(blank=True)
    body_ru = models.TextField(blank=True)
    body_en = models.TextField(blank=True)

class Ilmiy(models.Model):
    title_uz = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    body_uz = models.TextField(blank=True)
    body_ru = models.TextField(blank=True)
    body_en = models.TextField(blank=True)

class Yoshlar(models.Model):
    title_uz = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    body_uz = models.TextField(blank=True)
    body_ru = models.TextField(blank=True)
    body_en = models.TextField(blank=True)


class NormativHujatlar(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)
    fayl = models.FileField(upload_to='mormtiv_hujatlar')


class IchkiIdoraviyHujatlar(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)
    fayl = models.FileField(upload_to='mormtiv_hujatlar')


class XabarBerish(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)
    fayl = models.FileField(upload_to='mormtiv_hujatlar')

class XalqaroProfesorlarFikri(models.Model):
    title_uz = models.CharField(max_length=200, blank=True)
    title_ru = models.CharField(max_length=200, blank=True)
    title_en = models.CharField(max_length=200, blank=True)
    fikr_uz = models.TextField(blank=True)
    fikr_ru = models.TextField(blank=True)
    fikr_en = models.TextField(blank=True)
    fish_uz = models.CharField(max_length=200, blank=True)
    fish_ru = models.CharField(max_length=200, blank=True)
    fish_en = models.CharField(max_length=200, blank=True)
    lavozim_uz = models.CharField(max_length=200, blank=True)
    lavozim_ru = models.CharField(max_length=200, blank=True)
    lavozim_en = models.CharField(max_length=200, blank=True)
    rasm = models.ImageField(upload_to='xalqaro_profesorlar/', blank=True)
    link = models.URLField(max_length=500, blank=True)
