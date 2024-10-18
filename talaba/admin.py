from django.contrib import admin
from .models import BakalavrFanDasturKurs, BakalavrFanDasturYonalish, BakalavrFanDasturTuri, BakalavrFanDastur, BakalavrFanDasturTalimTuri
from .models import MagistrFanDasturKurs, MagistrFanDasturYonalish, MagistrFanDasturTuri, MagistrFanDastur

admin.site.register([BakalavrFanDasturKurs, BakalavrFanDasturYonalish, BakalavrFanDasturTuri, BakalavrFanDastur, BakalavrFanDasturTalimTuri])
admin.site.register([MagistrFanDasturKurs, MagistrFanDasturYonalish, MagistrFanDasturTuri, MagistrFanDastur])