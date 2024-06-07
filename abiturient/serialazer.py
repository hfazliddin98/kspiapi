from rest_framework import serializers 
from .models import CallMarkaz, AbiturientBakalavr , AbiturientMagistr, QabulHujjati



class CallMarkazSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallMarkaz
        fields = ( 
            'id',
            'title_uz', 
            'title_ru', 
            'title_en', 
            'body_uz', 
            'body_ru', 
            'body_en', 
            'tel_nomer_1',
            'tel_nomer_2',
            'tel_nomer_3',
            'tel_nomer_4',
            'tel_nomer_5'
        )


class QabulHujjatiSerializer(serializers.ModelSerializer):

    class Meta:
        model = QabulHujjati
        fields = ( 
            'id',
            'title', 
            'fayl',             
        )


class AbiturientBakalavrSerializer(serializers.ModelSerializer):

    class Meta:
        model = AbiturientBakalavr
        fields = ( 
            'id',
            'title_uz', 
            'title_ru', 
            'title_en', 
            'body_uz', 
            'body_ru', 
            'body_en', 
            'rasm'
        )

class AbiturientMagistrSerializer(serializers.ModelSerializer):

    class Meta:
        model = AbiturientMagistr
        fields = (
            'id', 
            'title_uz', 
            'title_ru', 
            'title_en', 
            'body_uz', 
            'body_ru', 
            'body_en', 
            'rasm'
        )


