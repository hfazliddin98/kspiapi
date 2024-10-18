from rest_framework import serializers # type: ignore
from .models import TalabaBakalavr, TalabaMagistr
from .models import BakalavrMalakaTalabi, BakalavrOquvRejaTuri, BakalavrOquvReja, BakalavrFanDasturTuri, BakalavrFanDastur, BakalavrFanKatalogi
from .models import BakalavrFanDasturKurs, BakalavrFanDasturYonalish, BakalavrFanDasturTalimTuri
from .models import MagistrMalakaTalabi, MagistrOquvRejaTuri, MagistrOquvReja, MagistrFanDasturTuri, MagistrFanDastur, MagistrFanKatalogi
from .models import MagistrFanDasturKurs, MagistrFanDasturYonalish
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


class BakalavrFanDasturKursSerializer(serializers.ModelSerializer):

    class Meta:
        model = BakalavrFanDasturKurs
        fields = '__all__'


class BakalavrFanDasturTalimTuriSerializer(serializers.ModelSerializer):

    class Meta:
        model = BakalavrFanDasturTalimTuri
        fields = '__all__'


class BakalavrFanDasturYonalishSerializer(serializers.ModelSerializer):

    class Meta:
        model = BakalavrFanDasturYonalish
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








class MagistrMalakaTalabiSerializer(serializers.ModelSerializer):

    class Meta:
        model = MagistrMalakaTalabi
        fields = '__all__'


class MagistrOquvRejaTuriSerializer(serializers.ModelSerializer):

    class Meta:
        model = MagistrOquvRejaTuri
        fields = '__all__'


class MagistrOquvRejaSerializer(serializers.ModelSerializer):

    class Meta:
        model = MagistrOquvReja
        fields = '__all__'


class MagistrFanDasturKursSerializer(serializers.ModelSerializer):

    class Meta:
        model = MagistrFanDasturKurs
        fields = '__all__'


class MagistrFanDasturYonalishSerializer(serializers.ModelSerializer):

    class Meta:
        model = MagistrFanDasturYonalish
        fields = '__all__'


class MagistrFanDasturTuriSerializer(serializers.ModelSerializer):

    class Meta:
        model = MagistrFanDasturTuri
        fields = '__all__'


class MagistrFanDasturSerializer(serializers.ModelSerializer):

    class Meta:
        model = MagistrFanDastur
        fields = '__all__'


class MagistrFanKatalogiSerializer(serializers.ModelSerializer):

    class Meta:
        model = MagistrFanKatalogi
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

