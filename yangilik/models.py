from django.db import models

UZ = 'uz'
RU = 'ru'
EN = 'en'

til_choices = {
    UZ : UZ,
    RU : RU,
    EN : EN
}


class Til(models.Model):
    name = models.CharField(max_length=5, choices = til_choices)

    def __str__(self):
        return self.name

class Yangilik(models.Model):
    til = models.ManyToManyField(Til)
    rasm_0 = models.ImageField(upload_to='yangilik/')
    rasm_1 = models.ImageField(upload_to='yangilik/', blank=True)
    rasm_2 = models.ImageField(upload_to='yangilik/', blank=True)
    rasm_3 = models.ImageField(upload_to='yangilik/', blank=True)
    rasm_4 = models.ImageField(upload_to='yangilik/', blank=True)
    title  = models.CharField(max_length=500)
    subtitle  = models.CharField(max_length=500, blank=True)
    body_0 = models.TextField()
    body_1 = models.TextField(blank=True)
    body_2 = models.TextField(blank=True)
    body_3 = models.TextField(blank=True)
    body_4 = models.TextField(blank=True)
    body_5 = models.TextField(blank=True)
    body_6 = models.TextField(blank=True)
    body_7 = models.TextField(blank=True)
    body_8 = models.TextField(blank=True)
    body_9 = models.TextField(blank=True)


    def __str__(self):
        return self.title
    

class Sinov(models.Model):
    # sinov = models.OneToOneRel(Yangilik, on_delete=models.SET_NULL, null=True, related_name='models', related_query_name='model')
    yangilik = models.ManyToManyField(Yangilik)


class Malumot(models.Model):
    son = models.IntegerField()
    data = models.ManyToManyField(Sinov)