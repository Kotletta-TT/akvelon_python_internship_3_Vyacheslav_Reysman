from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from transactions_api.models import Transact
from transactions_api.serializers import UserSerializer, TransactionSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This View-class to users information, auth users may read info about another users
    """
    queryset = User.objects.filter()
    serializer_class = UserSerializer


class UsersList(generics.RetrieveUpdateAPIView):
    """
    This view-class output all users payments
    default format:
        username
        sum(payments) for all time
    """


class TransactDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This CRUD-class to transaction information, user may create/change/delete info, only your transaction
    """