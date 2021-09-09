from rest_framework import serializers

from transactions_api.models import Transact


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    finance_now = serializers.DecimalField(max_digits=8, decimal_places=2, default=0.00)


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transact
        fields = ['date', 'amount']
