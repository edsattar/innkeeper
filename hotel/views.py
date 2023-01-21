from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers

# Create your views here.


class RoomTypeView(APIView):
    def get(self, request, format=None):
        room_types = models.RoomType.objects.all()
        serializer = serializers.RoomTypeSerializer(room_types, many=True)
        return Response(serializer.data)

class RoomView(APIView):
    def get(self, request, format=None):
        rooms = models.Room.objects.all()
        serializer = serializers.RoomSerializer(rooms, many=True)
        return Response(serializer.data)

class GuestView(APIView):
    def get(self, request, format=None):
        guests = models.Guest.objects.all()
        serializer = serializers.GuestSerializer(guests, many=True)
        return Response(serializer.data)

