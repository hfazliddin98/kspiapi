from rest_framework import serializers 
from .models import Jamoatchilik, Madaniy, Oquv, Akademik, Ilmiy, Yoshlar, NormativHujatlar, IchkiIdoraviyHujatlar, XabarBerish
from .models import XalqaroProfesorlarFikri, XalqaroHamkorlar


class JamoatchilikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jamoatchilik
        fields = '__all__'
        

class MadaniySerializer(serializers.ModelSerializer):
    class Meta:
        model = Madaniy
        fields = '__all__'        


class OquvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oquv
        fields = '__all__'        


class AkademikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Akademik
        fields = '__all__'


class IlmiySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ilmiy
        fields = '__all__'
        


class YoshlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yoshlar
        fields = '__all__'



class NormativHujatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormativHujatlar
        fields = '__all__'



class IchkiIdoraviyHujatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = IchkiIdoraviyHujatlar
        fields = '__all__'




class XabarBerishSerializer(serializers.ModelSerializer):
    class Meta:
        model = XabarBerish
        fields = '__all__'


class XalqaroProfesorlarFikriSerializer(serializers.ModelSerializer):
    class Meta:
        model = XalqaroProfesorlarFikri
        fields = '__all__'


class XalqaroHamkorlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = XalqaroHamkorlar
        fields = '__all__'
        

