from django.db import models


class InstitutHaqida(models.Model):

    bizning_maqsadimiz_title_uz = models.CharField(max_length=255, blank=True)
    bizning_maqsadimiz_title_ru = models.CharField(max_length=255, blank=True)
    bizning_maqsadimiz_title_en = models.CharField(max_length=255, blank=True)
    bizning_maqsadimiz_text_uz = models.TextField(blank=True)
    bizning_maqsadimiz_text_ru = models.TextField(blank=True)
    bizning_maqsadimiz_text_en = models.TextField(blank=True)

    biz_haqimizda_title_uz = models.CharField(max_length=255, blank=True)
    biz_haqimizda_title_ru = models.CharField(max_length=255, blank=True)
    biz_haqimizda_title_en = models.CharField(max_length=255, blank=True)
    biz_haqimizda_text_uz = models.TextField(blank=True)
    biz_haqimizda_text_ru = models.TextField(blank=True)
    biz_haqimizda_text_en = models.TextField(blank=True)

    institut_rasm = models.FileField(upload_to='institut_rasm/', blank=True)

    qoshimcha_title_uz = models.CharField(max_length=255, blank=True)
    qoshimcha_title_ru = models.CharField(max_length=255, blank=True)
    qoshimcha_title_en = models.CharField(max_length=255, blank=True)

    biz_kimmiz_title_uz = models.CharField(max_length=255, blank=True)
    biz_kimmiz_title_ru = models.CharField(max_length=255, blank=True)
    biz_kimmiz_title_en = models.CharField(max_length=255, blank=True)
    biz_kimmiz_text_uz = models.TextField(blank=True)
    biz_kimmiz_text_ru = models.TextField(blank=True)
    biz_kimmiz_text_en = models.TextField(blank=True)
    biz_kimmiz = models.FileField(upload_to='biz_kimmiz/', blank=True)

    qoshma_hamkorlar_title_uz = models.CharField(max_length=255, blank=True)
    qoshma_hamkorlar_title_ru = models.CharField(max_length=255, blank=True)
    qoshma_hamkorlar_title_en = models.CharField(max_length=255, blank=True)
    qoshma_hamkorlar_text_uz = models.TextField(blank=True)
    qoshma_hamkorlar_text_ru = models.TextField(blank=True)
    qoshma_hamkorlar_text_en = models.TextField(blank=True)
    qoshma_hamkorlar = models.FileField(upload_to='qoshma_hamkorlar/', blank=True)

    rivojlanayotgan_talabalar_hayoti_title_uz = models.CharField(max_length=255, blank=True)
    rivojlanayotgan_talabalar_hayoti_title_ru = models.CharField(max_length=255, blank=True)
    rivojlanayotgan_talabalar_hayoti_title_en = models.CharField(max_length=255, blank=True)
    rivojlanayotgan_talabalar_hayoti_text_uz = models.TextField(blank=True)
    rivojlanayotgan_talabalar_hayoti_text_ru = models.TextField(blank=True)
    rivojlanayotgan_talabalar_hayoti_text_en = models.TextField(blank=True)
    rivojlanayotgan_talabalar_hayoti = models.FileField(upload_to='rivojlanayotgan_talabalar_hayoti/', blank=True)

    kirish_title_uz = models.CharField(max_length=255, blank=True)
    kirish_title_ru = models.CharField(max_length=255, blank=True)
    kirish_title_en = models.CharField(max_length=255, blank=True)

    barcha_shakillar_title_uz = models.CharField(max_length=255, blank=True)
    barcha_shakillar_title_ru = models.CharField(max_length=255, blank=True)
    barcha_shakillar_title_en = models.CharField(max_length=255, blank=True)
    barcha_shakillar_text_uz = models.TextField(blank=True)
    barcha_shakillar_text_ru = models.TextField(blank=True)
    barcha_shakillar_text_en = models.TextField(blank=True)
    barcha_shakillar = models.FileField(upload_to='barcha_shakillar/', blank=True)

    
    moliyaviy_yordam_title_uz = models.CharField(max_length=255, blank=True)
    moliyaviy_yordam_title_ru = models.CharField(max_length=255, blank=True)
    moliyaviy_yordam_title_en = models.CharField(max_length=255, blank=True)
    moliyaviy_yordam_text_uz = models.TextField(blank=True)
    moliyaviy_yordam_text_ru = models.TextField(blank=True)
    moliyaviy_yordam_text_en = models.TextField(blank=True)
    moliyaviy_yordam = models.FileField(upload_to='moliyaviy_yordam/', blank=True)

    sport_bilan_birga_title_uz = models.CharField(max_length=255, blank=True)
    sport_bilan_birga_title_ru = models.CharField(max_length=255, blank=True)
    sport_bilan_birga_title_en = models.CharField(max_length=255, blank=True)
    sport_bilan_birga_text_uz = models.TextField(blank=True)
    sport_bilan_birga_text_ru = models.TextField(blank=True)
    sport_bilan_birga_text_en = models.TextField(blank=True)
    sport_bilan_birga = models.FileField(upload_to='sport_bilan_birga/', blank=True)




