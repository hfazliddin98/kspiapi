from rest_framework import serializers
from .models import Rektorat, Fakultet, Kafedra, Bolim, Markaz
from .models import RektoratRahbar, FakultetRahbar, KafedraRahbar, BolimRahbar, MarkazRahbar
from .models import RektoratHodim, FakultetHodim, KafedraHodim, BolimHodim, MarkazHodim



class RektoratSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rektorat
        fields = (
            'id',
            'name_uz',
            'name_ru',
            'name_en',
        )
        

class FakultetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fakultet
        fields = (
            'id',
            'name_uz',
            'name_ru',
            'name_en',
        )
        

class KafedraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kafedra
        fields = (
            'id',
            'name_uz',
            'name_ru',
            'name_en',
        )
        

class BolimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolim
        fields = (
            'id',
            'name_uz',
            'name_ru',
            'name_en',
        )
        

class MarkazSerializer(serializers.ModelSerializer):
    class Meta:
        model = Markaz
        fields = (
            'id',
            'name_uz',
            'name_ru',
            'name_en',
        )

class RektoratRahbarSerializer(serializers.ModelSerializer):
    rektorat_id = RektoratSerializer()
    class Meta:
        model = RektoratRahbar
        fields = (
            'id',
            'rektorat_id',
            'lavozim_uz',
            'lavozim_ru',
            'lavozim_en',
            'fish_uz',
            'fish_ru',
            'fish_en',
            'unvon_uz',
            'unvon_ru',
            'unvon_en',
            'qabul_soati_uz',
            'qabul_soati_ru',
            'qabul_soati_en',
            'telefon_nomer',
            'tg_username',
            'biografiya_uz',
            'biografiya_ru',
            'biografiya_en',
        )
        

class FakultetRahbarSerializer(serializers.ModelSerializer):
    fakultet_id = FakultetSerializer()
    class Meta:
        model = FakultetRahbar
        fields = (
            'id',
            'fakultet_id',
            'lavozim_uz',
            'lavozim_ru',
            'lavozim_en',
            'fish_uz',
            'fish_ru',
            'fish_en',
            'unvon_uz',
            'unvon_ru',
            'unvon_en',
            'qabul_soati_uz',
            'qabul_soati_ru',
            'qabul_soati_en',
            'telefon_nomer',
            'tg_username',
            'biografiya_uz',
            'biografiya_ru',
            'biografiya_en',
        )
        

class KafedraRahbarSerializer(serializers.ModelSerializer):
    kafedra_id = KafedraSerializer()
    class Meta:
        model = KafedraRahbar
        fields = (
            'id',
            'kafedra_id',
            'lavozim_uz',
            'lavozim_ru',
            'lavozim_en',
            'fish_uz',
            'fish_ru',
            'fish_en',
            'unvon_uz',
            'unvon_ru',
            'unvon_en',
            'qabul_soati_uz',
            'qabul_soati_ru',
            'qabul_soati_en',
            'telefon_nomer',
            'tg_username',
            'biografiya_uz',
            'biografiya_ru',
            'biografiya_en',
        )
        

class BolimRahbarSerializer(serializers.ModelSerializer):
    bolim_id = BolimSerializer()
    class Meta:
        model = BolimRahbar
        fields = (
            'id',
            'bolim_id',
            'lavozim_uz',
            'lavozim_ru',
            'lavozim_en',
            'fish_uz',
            'fish_ru',
            'fish_en',
            'unvon_uz',
            'unvon_ru',
            'unvon_en',
            'qabul_soati_uz',
            'qabul_soati_ru',
            'qabul_soati_en',
            'telefon_nomer',
            'tg_username',
            'biografiya_uz',
            'biografiya_ru',
            'biografiya_en',
        )
        

class MarkazRahbarSerializer(serializers.ModelSerializer):
    markaz_id = MarkazSerializer()
    class Meta:
        model = MarkazRahbar
        fields = (
            'id',
            'markaz_id',
            'lavozim_uz',
            'lavozim_ru',
            'lavozim_en',
            'fish_uz',
            'fish_ru',
            'fish_en',
            'unvon_uz',
            'unvon_ru',
            'unvon_en',
            'qabul_soati_uz',
            'qabul_soati_ru',
            'qabul_soati_en',
            'telefon_nomer',
            'tg_username',
            'biografiya_uz',
            'biografiya_ru',
            'biografiya_en',
        )

# Hodimlar

class RektoratHodimSerializer(serializers.ModelSerializer):
    rektorat_rahbar_id = RektoratRahbarSerializer()
    class Meta:
        model = RektoratHodim
        fields = (
            'id',
            'rektorat_rahbar_id',
            'lavozim_uz',
            'lavozim_ru',
            'lavozim_en',
            'fish_uz',
            'fish_ru',
            'fish_en',
            'unvon_uz',
            'unvon_ru',
            'unvon_en',
            'telefon_nomer',
        )
        

class FakultetHodimSerializer(serializers.ModelSerializer):
    fakultet_rahbar_id = FakultetRahbarSerializer()
    class Meta:
        model = FakultetHodim
        fields = (
            'id',
            'fakultet_rahbar_id',
            'lavozim_uz',
            'lavozim_ru',
            'lavozim_en',
            'fish_uz',
            'fish_ru',
            'fish_en',
            'unvon_uz',
            'unvon_ru',
            'unvon_en',
            'telefon_nomer',
        )
        

class KafedraHodimSerializer(serializers.ModelSerializer):
    kafedra_rahbar_id = KafedraRahbarSerializer()
    class Meta:
        model = KafedraHodim
        fields = (
            'id',
            'kafedra_rahbar_id',
            'lavozim_uz',
            'lavozim_ru',
            'lavozim_en',
            'fish_uz',
            'fish_ru',
            'fish_en',
            'unvon_uz',
            'unvon_ru',
            'unvon_en',
            'telefon_nomer',
        )
        

class BolimHodimSerializer(serializers.ModelSerializer):
    bolim_rahbar_id = BolimRahbarSerializer()
    class Meta:
        model = BolimHodim
        fields = (
            'id',
            'bolim_rahbar_id',
            'lavozim_uz',
            'lavozim_ru',
            'lavozim_en',
            'fish_uz',
            'fish_ru',
            'fish_en',
            'unvon_uz',
            'unvon_ru',
            'unvon_en',
            'telefon_nomer',
        )
        

class MarkazHodimSerializer(serializers.ModelSerializer):
    markaz_rahbar_id = MarkazRahbarSerializer()
    class Meta:
        model = MarkazHodim
        fields = (
            'id',
            'markaz_rahbar_id',
            'lavozim_uz',
            'lavozim_ru',
            'lavozim_en',
            'fish_uz',
            'fish_ru',
            'fish_en',
            'unvon_uz',
            'unvon_ru',
            'unvon_en',
            'telefon_nomer',
        )
        



