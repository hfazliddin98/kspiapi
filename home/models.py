from django.db import models    


class Yangilik(models.Model):
    rasm_1 = models.ImageField(upload_to='yangilik/', blank=True)   
    rasm_2 = models.ImageField(upload_to='yangilik/', blank=True)   
    rasm_3 = models.ImageField(upload_to='yangilik/', blank=True)   
    rasm_4 = models.ImageField(upload_to='yangilik/', blank=True)   
    rasm_5 = models.ImageField(upload_to='yangilik/', blank=True)   
    title_uz  = models.CharField(max_length=500, blank=True)
    title_ru  = models.CharField(max_length=500, blank=True)
    title_en  = models.CharField(max_length=500, blank=True)
    subtitle_uz  = models.CharField(max_length=500, blank=True)
    subtitle_ru  = models.CharField(max_length=500, blank=True)
    subtitle_en  = models.CharField(max_length=500, blank=True)
    body_0_uz = models.TextField(blank=True)
    body_0_ru = models.TextField(blank=True)
    body_0_en = models.TextField(blank=True)
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
    rasm = models.ImageField(upload_to='elon/', blank=True)
    title_uz  = models.CharField(max_length=1500, blank=True)
    title_ru  = models.CharField(max_length=1500, blank=True)
    title_en  = models.CharField(max_length=1500, blank=True)
    detail_uz = models.TextField(blank=True)
    detail_ru = models.TextField(blank=True)
    detail_en = models.TextField(blank=True)
    boshlanish_vaqti = models.CharField(max_length=500, blank=True)
    tugash_vaqti = models.CharField(max_length=500, blank=True)
    field_uz = models.TextField(blank=True)
    field_ru = models.TextField(blank=True)
    field_en = models.TextField(blank=True)
    adress_uz  = models.CharField(max_length=500, blank=True)
    adress_ru  = models.CharField(max_length=500, blank=True)
    adress_en  = models.CharField(max_length=500, blank=True)
    sana = models.DateTimeField(auto_now_add=True)


class GalareyaTuri(models.Model):
    tur_uz = models.CharField(max_length=500, blank=True)
    tur_ru = models.CharField(max_length=500, blank=True)
    tur_en = models.CharField(max_length=500, blank=True)

class Galareya(models.Model):
    tur_id = models.ForeignKey(GalareyaTuri, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='galareya/', blank=True)


class Fikr(models.Model):
    rasm = models.FileField(upload_to='fikr/', blank=True)
    video = models.FileField(upload_to='fikr/', blank=True)
    text_uz = models.CharField(max_length=200, blank=True)
    text_ru = models.CharField(max_length=200, blank=True)
    text_en = models.CharField(max_length=200, blank=True)
    talaba_uz = models.CharField(max_length=200, blank=True)
    talaba_ru = models.CharField(max_length=200, blank=True)
    talaba_en = models.CharField(max_length=200, blank=True)
    link = models.URLField(max_length=500, blank=True)


class Hamkorlarimiz(models.Model):
    hamkor_rasm = models.FileField(upload_to='hamkor_rasm', blank=True)


class Statistika(models.Model):
    statistika_title_uz = models.CharField(max_length=255, blank=True)
    statistika_title_ru = models.CharField(max_length=255, blank=True)
    statistika_title_en = models.CharField(max_length=255, blank=True)

    statistika_text_uz = models.TextField(blank=True)
    statistika_text_ru = models.TextField(blank=True)
    statistika_text_en = models.TextField(blank=True)

    talaba_title_uz = models.CharField(max_length=255, blank=True)
    talaba_title_ru = models.CharField(max_length=255, blank=True)
    talaba_title_en = models.CharField(max_length=255, blank=True)
    talaba_nomer = models.CharField(max_length=255, blank=True)
    
    phd_title_uz = models.CharField(max_length=255, blank=True)
    phd_title_ru = models.CharField(max_length=255, blank=True)
    phd_title_en = models.CharField(max_length=255, blank=True)
    phd_nomer = models.CharField(max_length=255, blank=True)

    oqituvchi_title_uz = models.CharField(max_length=255, blank=True)
    oqituvchi_title_ru = models.CharField(max_length=255, blank=True)
    oqituvchi_title_en = models.CharField(max_length=255, blank=True)
    oqituvchi_nomer = models.CharField(max_length=255, blank=True)

    fan_doktiri_title_uz = models.CharField(max_length=255, blank=True)
    fan_doktiri_title_ru = models.CharField(max_length=255, blank=True)
    fan_doktiri_title_en = models.CharField(max_length=255, blank=True)
    fan_doktiri_nomer = models.CharField(max_length=255, blank=True)


class Talaba(models.Model):
    talaba_rasm = models.ImageField(upload_to='talaba_rasm/', blank=True)

    talaba_coment_uz = models.CharField(max_length=255, blank=True)
    talaba_coment_ru = models.CharField(max_length=255, blank=True)
    talaba_coment_en = models.CharField(max_length=255, blank=True)

    talaba_ism_uz = models.CharField(max_length=255, blank=True)
    talaba_ism_ru = models.CharField(max_length=255, blank=True)
    talaba_ism_en = models.CharField(max_length=255, blank=True)

    talaba_inferior_uz = models.CharField(max_length=255, blank=True)
    talaba_inferior_ru = models.CharField(max_length=255, blank=True)
    talaba_inferior_en = models.CharField(max_length=255, blank=True)



    


    


    

