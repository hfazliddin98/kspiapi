from rest_framework import serializers # type: ignore
from .models import CallMarkaz, Bakalavr , Magistr, QabulHujjati



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


class BakalavrSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bakalavr
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

class MagistrSerializer(serializers.ModelSerializer):

    class Meta:
        model = Magistr
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


