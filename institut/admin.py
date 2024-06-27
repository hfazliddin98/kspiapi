from django.contrib import admin
from .models import InstitutHaqida, InstitutMalumotlari, Kengash, Tuzilma
from .models import InstitutRekviziti, BankRekviziti, Qabulxona

admin.site.register([
    InstitutHaqida, InstitutMalumotlari, Kengash, 
    Tuzilma, InstitutRekviziti, BankRekviziti, Qabulxona
])