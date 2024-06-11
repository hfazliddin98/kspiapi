from django.db import models


class Rektorat(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)


class Fakultet(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)


class Kafedra(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)


class Bolim(models.Model):
    name_uz = models.CharField(max_length=255, blank=True) 
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)


class Markaz(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)

class RektoratRahbar(models.Model):
    rektorat_id = models.ForeignKey(Rektorat, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='rahbarlar/')
    lavozim_uz = models.CharField(max_length=255, blank=True)
    lavozim_ru = models.CharField(max_length=255, blank=True)
    lavozim_en = models.CharField(max_length=255, blank=True)
    fish_uz = models.CharField(max_length=255, blank=True)
    fish_ru = models.CharField(max_length=255, blank=True)
    fish_en = models.CharField(max_length=255, blank=True)
    unvon_uz = models.CharField(max_length=255, blank=True)
    unvon_ru = models.CharField(max_length=255, blank=True)
    unvon_en = models.CharField(max_length=255, blank=True)
    qabul_soati_uz = models.CharField(max_length=255, blank=True)
    qabul_soati_ru = models.CharField(max_length=255, blank=True)
    qabul_soati_en = models.CharField(max_length=255, blank=True)
    telefon_nomer = models.CharField(max_length=255, blank=True)
    tg_username = models.CharField(max_length=255, blank=True)
    biografiya_uz = models.TextField(blank=True)
    biografiya_ru = models.TextField(blank=True)
    biografiya_en = models.TextField(blank=True)


class RektoratHodim(models.Model):
    rektorat_rahbar_id = models.ForeignKey(RektoratRahbar, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='rahbarlar/')
    lavozim_uz = models.CharField(max_length=255, blank=True)
    lavozim_ru = models.CharField(max_length=255, blank=True)
    lavozim_en = models.CharField(max_length=255, blank=True)
    fish_uz = models.CharField(max_length=255, blank=True)
    fish_ru = models.CharField(max_length=255, blank=True)
    fish_en = models.CharField(max_length=255, blank=True)
    unvon_uz = models.CharField(max_length=255, blank=True)
    unvon_ru = models.CharField(max_length=255, blank=True)
    unvon_en = models.CharField(max_length=255, blank=True)
    bolim_boshligi = models.BooleanField(default=False)
    telefon_nomer = models.CharField(max_length=255, blank=True)


class FakultetRahbar(models.Model):
    fakultet_id = models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='rahbarlar/')
    lavozim_uz = models.CharField(max_length=255, blank=True)
    lavozim_ru = models.CharField(max_length=255, blank=True)
    lavozim_en = models.CharField(max_length=255, blank=True)
    fish_uz = models.CharField(max_length=255, blank=True)
    fish_ru = models.CharField(max_length=255, blank=True)
    fish_en = models.CharField(max_length=255, blank=True)
    unvon_uz = models.CharField(max_length=255, blank=True)
    unvon_ru = models.CharField(max_length=255, blank=True)
    unvon_en = models.CharField(max_length=255, blank=True)
    qabul_soati_uz = models.CharField(max_length=255, blank=True)
    qabul_soati_ru = models.CharField(max_length=255, blank=True)
    qabul_soati_en = models.CharField(max_length=255, blank=True)
    telefon_nomer = models.CharField(max_length=255, blank=True)
    tg_username = models.CharField(max_length=255, blank=True)
    biografiya_uz = models.TextField(blank=True)
    biografiya_ru = models.TextField(blank=True)
    biografiya_en = models.TextField(blank=True)


class FakultetHodim(models.Model):
    fakultet_rahbar_id = models.ForeignKey(FakultetRahbar, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='rahbarlar/')
    lavozim_uz = models.CharField(max_length=255, blank=True)
    lavozim_ru = models.CharField(max_length=255, blank=True)
    lavozim_en = models.CharField(max_length=255, blank=True)
    fish_uz = models.CharField(max_length=255, blank=True)
    fish_ru = models.CharField(max_length=255, blank=True)
    fish_en = models.CharField(max_length=255, blank=True)
    unvon_uz = models.CharField(max_length=255, blank=True)
    unvon_ru = models.CharField(max_length=255, blank=True)
    unvon_en = models.CharField(max_length=255, blank=True)
    bolim_boshligi = models.BooleanField(default=False)
    telefon_nomer = models.CharField(max_length=255, blank=True)


class KafedraRahbar(models.Model):
    kafedra_id = models.ForeignKey(Kafedra, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='rahbarlar/')
    lavozim_uz = models.CharField(max_length=255, blank=True)
    lavozim_ru = models.CharField(max_length=255, blank=True)
    lavozim_en = models.CharField(max_length=255, blank=True)
    fish_uz = models.CharField(max_length=255, blank=True)
    fish_ru = models.CharField(max_length=255, blank=True)
    fish_en = models.CharField(max_length=255, blank=True)
    unvon_uz = models.CharField(max_length=255, blank=True)
    unvon_ru = models.CharField(max_length=255, blank=True)
    unvon_en = models.CharField(max_length=255, blank=True)
    qabul_soati_uz = models.CharField(max_length=255, blank=True)
    qabul_soati_ru = models.CharField(max_length=255, blank=True)
    qabul_soati_en = models.CharField(max_length=255, blank=True)
    telefon_nomer = models.CharField(max_length=255, blank=True)
    tg_username = models.CharField(max_length=255, blank=True)
    biografiya_uz = models.TextField(blank=True)
    biografiya_ru = models.TextField(blank=True)
    biografiya_en = models.TextField(blank=True)


class KafedraHodim(models.Model):
    kafedra_rahbar_id = models.ForeignKey(KafedraRahbar, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='rahbarlar/')
    lavozim_uz = models.CharField(max_length=255, blank=True)
    lavozim_ru = models.CharField(max_length=255, blank=True)
    lavozim_en = models.CharField(max_length=255, blank=True)
    fish_uz = models.CharField(max_length=255, blank=True)
    fish_ru = models.CharField(max_length=255, blank=True)
    fish_en = models.CharField(max_length=255, blank=True)
    unvon_uz = models.CharField(max_length=255, blank=True)
    unvon_ru = models.CharField(max_length=255, blank=True)
    unvon_en = models.CharField(max_length=255, blank=True)
    bolim_boshligi = models.BooleanField(default=False)
    telefon_nomer = models.CharField(max_length=255, blank=True)


class BolimRahbar(models.Model):
    bolim_id = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='rahbarlar/')
    lavozim_uz = models.CharField(max_length=255, blank=True)
    lavozim_ru = models.CharField(max_length=255, blank=True)
    lavozim_en = models.CharField(max_length=255, blank=True)
    fish_uz = models.CharField(max_length=255, blank=True)
    fish_ru = models.CharField(max_length=255, blank=True)
    fish_en = models.CharField(max_length=255, blank=True)
    unvon_uz = models.CharField(max_length=255, blank=True)
    unvon_ru = models.CharField(max_length=255, blank=True)
    unvon_en = models.CharField(max_length=255, blank=True)
    qabul_soati_uz = models.CharField(max_length=255, blank=True)
    qabul_soati_ru = models.CharField(max_length=255, blank=True)
    qabul_soati_en = models.CharField(max_length=255, blank=True)
    telefon_nomer = models.CharField(max_length=255, blank=True)
    tg_username = models.CharField(max_length=255, blank=True)
    biografiya_uz = models.TextField(blank=True)
    biografiya_ru = models.TextField(blank=True)
    biografiya_en = models.TextField(blank=True)


class BolimHodim(models.Model):
    bolim_rahbar_id = models.ForeignKey(BolimRahbar, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='rahbarlar/')
    lavozim_uz = models.CharField(max_length=255, blank=True)
    lavozim_ru = models.CharField(max_length=255, blank=True)
    lavozim_en = models.CharField(max_length=255, blank=True)
    fish_uz = models.CharField(max_length=255, blank=True)
    fish_ru = models.CharField(max_length=255, blank=True)
    fish_en = models.CharField(max_length=255, blank=True)
    unvon_uz = models.CharField(max_length=255, blank=True)
    unvon_ru = models.CharField(max_length=255, blank=True)
    unvon_en = models.CharField(max_length=255, blank=True)
    bolim_boshligi = models.BooleanField(default=False)
    telefon_nomer = models.CharField(max_length=255, blank=True)


class MarkazRahbar(models.Model):
    markaz_id = models.ForeignKey(Markaz, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='rahbarlar/')
    lavozim_uz = models.CharField(max_length=255, blank=True)
    lavozim_ru = models.CharField(max_length=255, blank=True)
    lavozim_en = models.CharField(max_length=255, blank=True)
    fish_uz = models.CharField(max_length=255, blank=True)
    fish_ru = models.CharField(max_length=255, blank=True)
    fish_en = models.CharField(max_length=255, blank=True)
    unvon_uz = models.CharField(max_length=255, blank=True)
    unvon_ru = models.CharField(max_length=255, blank=True)
    unvon_en = models.CharField(max_length=255, blank=True)
    qabul_soati_uz = models.CharField(max_length=255, blank=True)
    qabul_soati_ru = models.CharField(max_length=255, blank=True)
    qabul_soati_en = models.CharField(max_length=255, blank=True)
    telefon_nomer = models.CharField(max_length=255, blank=True)
    tg_username = models.CharField(max_length=255, blank=True)
    biografiya_uz = models.TextField(blank=True)
    biografiya_ru = models.TextField(blank=True)
    biografiya_en = models.TextField(blank=True)


class MarkazHodim(models.Model):
    markaz_rahbar_id = models.ForeignKey(MarkazRahbar, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='rahbarlar/')
    lavozim_uz = models.CharField(max_length=255, blank=True)
    lavozim_ru = models.CharField(max_length=255, blank=True)
    lavozim_en = models.CharField(max_length=255, blank=True)
    fish_uz = models.CharField(max_length=255, blank=True)
    fish_ru = models.CharField(max_length=255, blank=True)
    fish_en = models.CharField(max_length=255, blank=True)
    unvon_uz = models.CharField(max_length=255, blank=True)
    unvon_ru = models.CharField(max_length=255, blank=True)
    unvon_en = models.CharField(max_length=255, blank=True)
    bolim_boshligi = models.BooleanField(default=False)
    telefon_nomer = models.CharField(max_length=255, blank=True)

