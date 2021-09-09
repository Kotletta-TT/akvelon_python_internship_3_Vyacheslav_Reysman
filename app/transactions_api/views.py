from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from transactions_api.models import Transact
from transactions_api.serializers import UserSerializer, TransactionSerializer


class MeDetail(APIView):
    """
    This CRUD-class to yourself information, user may create/read/update/delete info, only about yourself
    """

class UserDetail(APIView):
    """
    This View-class to users information, auth users may read info about another users
    """
    def get(self, request, pk):
        queryset = User.objects.filter(id=pk)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)


class UsersList():
    """
    This view-class output all users payments
    default format:
        username
        sum(payments) for all time
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TransactDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This CRUD-class to transaction information, user may create/change/delete info, only your transaction
    """
    queryset = Transact.objects.all()
    serializer_class = TransactionSerializer