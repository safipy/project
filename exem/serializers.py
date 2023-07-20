from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from .models import Exem


class ExemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exem
        fields = "title description completed".split()


class ExemValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exem
        fields = "__all__"
