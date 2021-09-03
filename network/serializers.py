from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.utils import timezone

class TrustedNetworkSerializers(serializers.Serializer):
    user = serializers.SerializerMethodField()
    domain = serializers.CharField()
    email = serializers.CharField()

    def get_user(self,obj):
        return obj.user.username