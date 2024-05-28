from rest_framework import serializers # type: ignore
from .models import CallMarkaz



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
            'tel_nomer'
        )


