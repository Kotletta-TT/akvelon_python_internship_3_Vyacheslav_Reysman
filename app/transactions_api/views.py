from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from transactions_api.models import Transact
from transactions_api.serializers import UserCustomSerializer, \
    TransactListSerializer, TransactIdSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This View-class to users information, auth users may read info about
    another users
    """
    queryset = User.objects.filter()
    serializer_class = UserCustomSerializer
    permission_classes = [permissions.IsAuthenticated]


class UsersList(generics.RetrieveUpdateAPIView):
    """
    This view-class output all users payments
    default format:
        username
        sum(payments) for all time
    """
    queryset = User.objects.all()
    serializer_class = UserCustomSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransactDetail(generics.RetrieveUpdateDestroyAPIView,
                     generics.CreateAPIView):
    """
    This CRUD-class to transaction information, user may 
    create/change/delete info, only your transaction
    """
    queryset = Transact.objects.filter()
    serializer_class = TransactIdSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransactList(generics.ListAPIView):
    queryset = Transact.objects.all()
    serializer_class = TransactListSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransactId(APIView):
    def get(self, request, pk):
        transact = Transact.objects.get(id=pk)
        serializer = TransactListSerializer(transact)
        return Response(serializer.data)
