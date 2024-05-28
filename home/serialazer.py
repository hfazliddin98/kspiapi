from rest_framework import serializers # type: ignore
from .models import Yangilik, Elon, GalareyaTuri, Galareya, Fikr, Statistika, Hamkorlarimiz, Talaba, ElektronKutubxona, VideoMaruzalar, VirtualQabulxona, MasofaviyTalim, Fakultet
from .models import NavbarName, NavbarLink


class YangilikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangilik
        fields = '__all__'
        

class ElonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elon
        fields = '__all__'
        


class GalareyaTuriSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalareyaTuri
        fields = '__all__'
        


class GalareyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Galareya
        fields = '__all__'


class FikrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fikr
        fields = '__all__'
        


class StatistikaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistika
        fields = '__all__'
        

class HamkorlarimizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hamkorlarimiz
        fields = '__all__'
        

class TalabaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talaba
        fields = '__all__'
        

class ElektronKutubxonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElektronKutubxona
        fields = '__all__'


class VirtualQabulxonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualQabulxona
        fields = '__all__'

class MasofaviyTalimSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasofaviyTalim
        fields = '__all__'


# yangi qoshilgan kodlar

class FakultetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fakultet
        fields = ('id', 'name_uz', 'name_ru', 'name_en')

class VideoMaruzalarSerializer(serializers.ModelSerializer):
    fakultet_id = FakultetSerializer()

    class Meta:
        model = VideoMaruzalar
        fields = ('id', 'link', 'video', 'fakultet_id')


class NavbarNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = NavbarName
        fields = ('id', 'name_uz', 'name_ru', 'name_en')


class NavbarLinkSerializer(serializers.ModelSerializer):
    navbar_name_id = NavbarNameSerializer()

    class Meta:
        model = NavbarLink
        fields = ('id', 'link', 'navbar_name_id')