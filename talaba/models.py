from django.db import models

class TalabaBakalavr(models.Model):
    title_uz = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    body_uz = models.TextField(blank=True)
    body_ru = models.TextField(blank=True)
    body_en = models.TextField(blank=True)
    rasm = models.ImageField(upload_to='bakalavr/', blank=True)
    

class TalabaMagistr(models.Model):
    title_uz = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    body_uz = models.TextField(blank=True)
    body_ru = models.TextField(blank=True)
    body_en = models.TextField(blank=True)
    rasm = models.ImageField(upload_to='magistr/', blank=True)


class BakalavrMalakaTalabi(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)
    fayl = models.FileField(upload_to='malaka_talab/')
    sana = models.CharField(max_length=255, blank=True)

class BakalavrOquvRejaTuri(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)

class BakalavrOquvReja(models.Model):
    oquv_reja_turi_id = models.ForeignKey(BakalavrOquvRejaTuri, on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)
    fayl = models.FileField(upload_to='oquv_reja/')
    sana = models.CharField(max_length=255, blank=True)

class BakalavrFanDasturTuri(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)

class BakalavrFanDastur(models.Model):
    fan_dastur_turi_id = models.ForeignKey(BakalavrFanDasturTuri, on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)
    fayl = models.FileField(upload_to='fan_dastur/')
    sana = models.CharField(max_length=255, blank=True)

class BakalavrFanKatalogi(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)
    fayl = models.FileField(upload_to='fan_katalogi/')
    sana = models.CharField(max_length=255, blank=True)
