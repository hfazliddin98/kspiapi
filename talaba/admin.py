from django.contrib import admin
from .models import BakalavrFanDasturKurs, BakalavrFanDasturYonalish, BakalavrFanDasturTuri, BakalavrFanDastur
from .models import MagistrFanDasturKurs, MagistrFanDasturYonalish, MagistrFanDasturTuri, MagistrFanDastur

admin.site.register([BakalavrFanDasturKurs, BakalavrFanDasturYonalish, BakalavrFanDasturTuri, BakalavrFanDastur])
admin.site.register([MagistrFanDasturKurs, MagistrFanDasturYonalish, MagistrFanDasturTuri, MagistrFanDastur])