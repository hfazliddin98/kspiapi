from django.contrib import admin
from .models import Rektorat, Fakultet, Kafedra, Bolim, Markaz
from .models import RektoratRahbar, FakultetRahbar, KafedraRahbar, BolimRahbar, MarkazRahbar
from .models import RektoratHodim, FakultetHodim, KafedraHodim, BolimHodim, MarkazHodim


admin.site.register([
    Rektorat, Fakultet, Kafedra, Bolim, Markaz,
    RektoratRahbar, FakultetRahbar, KafedraRahbar, BolimRahbar, MarkazRahbar,
    RektoratHodim, FakultetHodim, KafedraHodim, BolimHodim, MarkazHodim,
])