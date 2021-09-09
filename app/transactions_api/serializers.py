from django.contrib.auth.models import User
from rest_framework import serializers

from transactions_api.models import Transact


class UserCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['username', 'email', 'first_name', 'last_name']


class TransactListSerializer(serializers.Serializer):
    user = serializers.SlugRelatedField(slug_field='profile', read_only=True)
    date = serializers.DateField()
    amount = serializers.DecimalField(max_digits=8, decimal_places=2)
    class Meta:
        model = Transact
        fields = '__all__'


class TransactIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transact
        fields = ['date', 'amount']

class TransactUserSerializer(serializers.Serializer):
    pass