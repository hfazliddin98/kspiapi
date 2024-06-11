from rest_framework import serializers
from django.contrib.auth.models import User
from home.models import Yangilik, Elon

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class YangilikSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangilik
        fields = "__all__"

class ElonSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elon
        fields = "__all__"