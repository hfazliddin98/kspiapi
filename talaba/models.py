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
    


class MagistrMalakaTalabi(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)
    fayl = models.FileField(upload_to='malaka_talab/')
    sana = models.CharField(max_length=255, blank=True)

class MagistrOquvRejaTuri(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)

class MagistrOquvReja(models.Model):
    oquv_reja_turi_id = models.ForeignKey(MagistrOquvRejaTuri, on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)
    fayl = models.FileField(upload_to='oquv_reja/')
    sana = models.CharField(max_length=255, blank=True)

class MagistrFanDasturTuri(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)

class MagistrFanDastur(models.Model):
    fan_dastur_turi_id = models.ForeignKey(MagistrFanDasturTuri, on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)
    fayl = models.FileField(upload_to='fan_dastur/')
    sana = models.CharField(max_length=255, blank=True)

class MagistrFanKatalogi(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)
    fayl = models.FileField(upload_to='fan_katalogi/')
    sana = models.CharField(max_length=255, blank=True)




class TTJRahbar(models.Model):
    title_uz = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    body_uz = models.CharField(max_length=255, blank=True)
    body_ru = models.CharField(max_length=255, blank=True)
    body_en = models.CharField(max_length=255, blank=True)
    rasm = models.ImageField(upload_to='ttjrahbar', blank=True)
    rahbar_fish = models.CharField(max_length=255, blank=True)

class TTJStatistika(models.Model):
    talabalar = models.CharField(max_length=255, blank=True)
    xonalar = models.CharField(max_length=255, blank=True)
    binolar = models.CharField(max_length=255, blank=True)

class TTJAriza(models.Model):
    link_1_title_uz = models.CharField(max_length=255, blank=True)
    link_1_title_ru = models.CharField(max_length=255, blank=True)
    link_1_title_en = models.CharField(max_length=255, blank=True)
    link_1 = models.CharField(max_length=255, blank=True)
    link_2_title_uz = models.CharField(max_length=255, blank=True)
    link_2_title_ru = models.CharField(max_length=255, blank=True)
    link_2_title_en = models.CharField(max_length=255, blank=True)
    link_2 = models.CharField(max_length=255, blank=True)
    link_3_title_uz = models.CharField(max_length=255, blank=True)
    link_3_title_ru = models.CharField(max_length=255, blank=True)
    link_3_title_en = models.CharField(max_length=255, blank=True)
    link_3 = models.CharField(max_length=255, blank=True)

class TTJCampus(models.Model):
    title_uz = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    body_uz = models.CharField(max_length=255, blank=True)
    body_ru = models.CharField(max_length=255, blank=True)
    body_en = models.CharField(max_length=255, blank=True)
    rasm = models.ImageField(upload_to='ttjcampus', blank=True)
