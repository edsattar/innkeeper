from rest_framework import serializers
from . import models

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RoomType
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = '__all__'

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Guest
        fields = '__all__'