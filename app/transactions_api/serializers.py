from rest_framework import serializers
from django.contrib.auth.models import User

from transactions_api.models import Transact


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transact
        fields = '__all__'