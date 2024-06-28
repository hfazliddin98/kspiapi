from rest_framework import serializers # type: ignore
from .models import TalabaBakalavr, TalabaMagistr
from .models import BakalavrMalakaTalabi, BakalavrOquvRejaTuri, BakalavrOquvReja, BakalavrFanDasturTuri, BakalavrFanDastur, BakalavrFanKatalogi
from  .models import TTJAriza, TTJCampus, TTJRahbar, TTJStatistika




class TalabaBakalavrSerializer(serializers.ModelSerializer):

    class Meta:
        model = TalabaBakalavr
        fields = '__all__'


class TalabaMagistrSerializer(serializers.ModelSerializer):

    class Meta:
        model = TalabaMagistr
        fields = '__all__'


class BakalavrMalakaTalabiSerializer(serializers.ModelSerializer):

    class Meta:
        model = BakalavrMalakaTalabi
        fields = '__all__'


class BakalavrOquvRejaTuriSerializer(serializers.ModelSerializer):

    class Meta:
        model = BakalavrOquvRejaTuri
        fields = '__all__'


class BakalavrOquvRejaSerializer(serializers.ModelSerializer):

    class Meta:
        model = BakalavrOquvReja
        fields = '__all__'


class BakalavrFanDasturTuriSerializer(serializers.ModelSerializer):

    class Meta:
        model = BakalavrFanDasturTuri
        fields = '__all__'


class BakalavrFanDasturSerializer(serializers.ModelSerializer):

    class Meta:
        model = BakalavrFanDastur
        fields = '__all__'


class BakalavrFanKatalogiSerializer(serializers.ModelSerializer):

    class Meta:
        model = BakalavrFanKatalogi
        fields = '__all__'


class TTJArizaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TTJAriza
        fields = '__all__'

class TTJCampusSerializer(serializers.ModelSerializer):

    class Meta:
        model = TTJCampus
        fields = '__all__'

class TTJRahbarSerializer(serializers.ModelSerializer):

    class Meta:
        model = TTJRahbar
        fields = '__all__'

class TTJStatistikaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TTJStatistika
        fields = '__all__'

