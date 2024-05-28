from django.db import models

class CallMarkaz(models.Model):
    title_uz = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    body_uz = models.TextField(blank=True)
    body_ru = models.TextField(blank=True)
    body_en = models.TextField(blank=True)
    tel_nomer = models.TextField(blank=True)
