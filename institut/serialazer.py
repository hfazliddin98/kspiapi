from rest_framework import serializers
from .models import InstitutHaqida, InstitutMalumotlari, Kengash, Tuzilma, InstitutRekviziti, BankRekviziti, Qabulxona

class InstitutHaqidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutHaqida
        fields = (
            'title_uz',
            'title_ru',
            'title_en',
            'body_uz',
            'body_ru',
            'body_en',
            'rasm',
            'fayl',
        )
        
class InstitutMalumotlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutMalumotlari
        fields = (
            'title_uz',
            'title_ru',
            'title_en',
            'body_uz',
            'body_ru',
            'body_en',
            'rasm',
            'fayl',
        )

class KengashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kengash
        fields = (
            'fish', 
            'telefon', 
            'email', 
            'kengash_vazifasi', 
            'kengash_haqida'
        )


class TuzilmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuzilma
        fields = (
            'name_uz',
            'name_ru',
            'name_en',
            'rasm_1',
            'rasm_2',
            'rasm_3',
            'rasm_4',
            'rasm_5',
            'pdf_fayl'
        )


class InstitutRekvizitiSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutRekviziti
        fields = (
            'name_uz',
            'name_ru',
            'name_en',
            'qiymat_uz',
            'qiymat_ru',
            'qiymat_en',
        )


class BankRekvizitiSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankRekviziti
        fields = (
            'name_uz',
            'name_ru',
            'name_en',
            'qiymat_uz',
            'qiymat_ru',
            'qiymat_en',
        )


class QabulxonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qabulxona
        fields = (
            'fish',
            'telefon_nomer',
            'email',
            'mavzu',
            'xabar'
        )


