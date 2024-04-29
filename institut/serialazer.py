from rest_framework import serializers
from .models import InstitutHaqida

class InstitutHaqidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutHaqida
        fields = '__all__'
        depth = 3

