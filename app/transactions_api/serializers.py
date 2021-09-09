from rest_framework import serializers
from django.contrib.auth.models import User

from transactions_api.models import Transact


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transact
        fields = ['date', 'amount']
