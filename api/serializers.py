from rest_framework import serializers
from .models import CrashLog, UserInfo
from django.contrib.auth.models import User
import pdb

class EmergencyContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('contacts',)

class CrashLogSerializer(serializers.ModelSerializer):
    longitude = serializers.ReadOnlyField(source='log.longitude')
    latitude = serializers.ReadOnlyField(source='log.latitude')
    heart_rate = serializers.ReadOnlyField(source='log.heart_rate')
    video_id = serializers.ReadOnlyField(source='recorded_crash')

    class Meta:
        model = CrashLog
        fields = ('longitude', 'latitude', 'heart_rate', 'save_time', 'video_id')

class CrashPointSerializer(serializers.ModelSerializer):
    longitude = serializers.SerializerMethodField()
    latitude = serializers.SerializerMethodField()

    class Meta:
        model = CrashLog
        fields = ('longitude', 'latitude')

    def get_longitude(self, obj):
        return float(obj.log.get('longitude'))

    def get_latitude(self, obj):
        return float(obj.log.get('latitude'))

class LivePointSerializer(serializers.ModelSerializer):
    longitude = serializers.SerializerMethodField()
    latitude = serializers.SerializerMethodField()
    mine = serializers.SerializerMethodField()

    class Meta:
        model = CrashLog
        fields = ('id', 'longitude', 'latitude', 'state', 'mine')

    def get_longitude(self, obj):
        return float(obj.log.get('longitude'))

    def get_latitude(self, obj):
        return float(obj.log.get('latitude'))

    def get_mine(self, obj):
        return self.context['request'].user == obj.attending_emergency_provider