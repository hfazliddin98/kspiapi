from rest_framework import serializers 
from .models import CallMarkaz, AbiturientBakalavr , AbiturientMagistr, QabulHujjati
from .models import BaxoMezoni, Kvota



class CallMarkazSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallMarkaz
        fields = '__all__'


class QabulHujjatiSerializer(serializers.ModelSerializer):

    class Meta:
        model = QabulHujjati
        fields = '__all__'


class AbiturientBakalavrSerializer(serializers.ModelSerializer):

    class Meta:
        model = AbiturientBakalavr
        fields = '__all__'

class AbiturientMagistrSerializer(serializers.ModelSerializer):

    class Meta:
        model = AbiturientMagistr
        fields = '__all__'


class BaxoMezoniSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaxoMezoni
        fields = '__all__'


class KvotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kvota
        fields = '__all__'
