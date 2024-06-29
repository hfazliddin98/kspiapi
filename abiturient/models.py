from django.db import models

class CallMarkaz(models.Model):
    title_uz = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    body_uz = models.TextField(blank=True)
    body_ru = models.TextField(blank=True)
    body_en = models.TextField(blank=True)
    tel_nomer_1 = models.CharField(max_length=255, blank=True)
    tel_nomer_2 = models.CharField(max_length=255, blank=True)
    tel_nomer_3 = models.CharField(max_length=255, blank=True)
    tel_nomer_4 = models.CharField(max_length=255, blank=True)
    tel_nomer_5 = models.CharField(max_length=255, blank=True)

class QabulHujjati(models.Model):
    title = models.CharField(max_length=255, blank=True)
    fayl = models.FileField(upload_to='qabulhujati/', blank=True)

class AbiturientBakalavr(models.Model):
    title_uz = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    body_uz = models.TextField(blank=True)
    body_ru = models.TextField(blank=True)
    body_en = models.TextField(blank=True)
    rasm = models.ImageField(upload_to='bakalavr/', blank=True)
    

class AbiturientMagistr(models.Model):
    title_uz = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    body_uz = models.TextField(blank=True)
    body_ru = models.TextField(blank=True)
    body_en = models.TextField(blank=True)
    rasm = models.ImageField(upload_to='magistr/', blank=True)


class BaxoMezoni(models.Model):
    title_uz = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    fayl = models.FileField(upload_to='mezon', blank=True)


class Kvota(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)
    fayl = models.FileField(upload_to='mezon', blank=True)