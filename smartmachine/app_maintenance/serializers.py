from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Fault, FaultCode, Status


class FaultSerializer(serializers.ModelSerializer):

    code = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        queryset=FaultCode.objects.all(),
        slug_field='id')

    class Meta:
        model = Fault
        fields = ['id', 'code', 'start', 'end', 'product', 'pallet', 'operator', ]


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ['id', 'type', 'station', 'start', 'end', ]
