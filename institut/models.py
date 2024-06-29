from django.db import models


class InstitutHaqida(models.Model):
    title_uz = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    body_uz = models.TextField(blank=True)
    body_ru = models.TextField(blank=True)
    body_en = models.TextField(blank=True)
    rasm = models.ImageField(upload_to='tadbir/rasm/', blank=True)
    fayl = models.FileField(upload_to='tadbir/fayl/', blank=True)


class InstitutMalumotlari(models.Model):
    title_uz = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    body_uz = models.TextField(blank=True)
    body_ru = models.TextField(blank=True)
    body_en = models.TextField(blank=True)
    rasm = models.ImageField(upload_to='tadbir/rasm/', blank=True)
    fayl = models.FileField(upload_to='tadbir/fayl/', blank=True)



class Kengash(models.Model):
    fish_uz = models.CharField(max_length=255, blank=True)
    fish_ru = models.CharField(max_length=255, blank=True)
    fish_en = models.CharField(max_length=255, blank=True)
    telefon = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    kengash_vazifasi_uz = models.TextField(blank=True)
    kengash_vazifasi_ru = models.TextField(blank=True)
    kengash_vazifasi_en = models.TextField(blank=True)
    kengash_haqida_uz = models.TextField(blank=True)
    kengash_haqida_ru = models.TextField(blank=True)
    kengash_haqida_en = models.TextField(blank=True)
    rasm = models.ImageField(upload_to='kengash/', blank=True)


class Tuzilma(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)
    rasm_1 = models.ImageField(upload_to='tuzilma/', blank=True)
    rasm_2 = models.ImageField(upload_to='tuzilma/', blank=True)
    rasm_3 = models.ImageField(upload_to='tuzilma/', blank=True)
    rasm_4 = models.ImageField(upload_to='tuzilma/', blank=True)
    rasm_5 = models.ImageField(upload_to='tuzilma/', blank=True)
    pdf_fayl = models.FileField(upload_to='tuzilma/', blank=True)


class InstitutRekviziti(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)
    qiymat_uz = models.CharField(max_length=255, blank=True)
    qiymat_ru = models.CharField(max_length=255, blank=True)
    qiymat_en = models.CharField(max_length=255, blank=True)


class BankRekviziti(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)
    qiymat_uz = models.CharField(max_length=255, blank=True)
    qiymat_ru = models.CharField(max_length=255, blank=True)
    qiymat_en = models.CharField(max_length=255, blank=True)
    

class Qabulxona(models.Model):
    fish = models.CharField(max_length=255, blank=True)
    telefon_nomer = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    mavzu = models.TextField(blank=True)
    xabar = models.TextField(blank=True)