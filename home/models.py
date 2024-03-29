from django.db import models    


class Yangilik(models.Model):
    rasm_1 = models.ImageField(upload_to='yangilik/')   
    rasm_2 = models.ImageField(upload_to='yangilik/', blank=True)   
    rasm_3 = models.ImageField(upload_to='yangilik/', blank=True)   
    rasm_4 = models.ImageField(upload_to='yangilik/', blank=True)   
    rasm_5 = models.ImageField(upload_to='yangilik/', blank=True)   
    title_uz  = models.CharField(max_length=500)
    title_ru  = models.CharField(max_length=500)
    title_en  = models.CharField(max_length=500)
    subtitle_uz  = models.CharField(max_length=500, blank=True)
    subtitle_ru  = models.CharField(max_length=500, blank=True)
    subtitle_en  = models.CharField(max_length=500, blank=True)
    body_0_uz = models.TextField()
    body_0_ru = models.TextField()
    body_0_en = models.TextField()
    body_1_uz = models.TextField(blank=True)
    body_1_ru = models.TextField(blank=True)
    body_1_en = models.TextField(blank=True)
    body_2_uz = models.TextField(blank=True)
    body_2_ru = models.TextField(blank=True)
    body_2_en = models.TextField(blank=True)
    body_3_uz = models.TextField(blank=True)
    body_3_ru = models.TextField(blank=True)
    body_3_en = models.TextField(blank=True)
    body_4_uz = models.TextField(blank=True)
    body_4_ru = models.TextField(blank=True)
    body_4_en = models.TextField(blank=True)
    body_5_uz = models.TextField(blank=True)
    body_5_ru = models.TextField(blank=True)
    body_5_en = models.TextField(blank=True)
    body_6_uz = models.TextField(blank=True)
    body_6_ru = models.TextField(blank=True)
    body_6_en = models.TextField(blank=True)
    body_7_uz = models.TextField(blank=True)
    body_7_ru = models.TextField(blank=True)
    body_7_en = models.TextField(blank=True)
    body_8_uz = models.TextField(blank=True)
    body_8_ru = models.TextField(blank=True)
    body_8_en = models.TextField(blank=True)
    body_9_uz = models.TextField(blank=True)
    body_9_ru = models.TextField(blank=True)
    body_9_en = models.TextField(blank=True)
    sana = models.CharField(max_length=500, blank=True)


class Elon(models.Model):
    rasm = models.ImageField(upload_to='elon/')
    title  = models.CharField(max_length=1500)
    detail = models.TextField()
    boshlanish_vaqti = models.CharField(max_length=500)
    tugash_vaqti = models.CharField(max_length=500)
    field = models.TextField()
    adress  = models.CharField(max_length=500)
    sana = models.DateTimeField(auto_now_add=True)


class GalareyaTuri(models.Model):
    tur = models.CharField(max_length=500)

class Galareya(models.Model):
    tur_id = models.ForeignKey(GalareyaTuri, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='galareya/')


    


    


    

