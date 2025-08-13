from django.shortcuts import render

from rest_framework import generics
from .models import inscrito
from .serializers import InscritoSerializer
class InscritoList(generics.ListCreateAPIView):
    queryset = inscrito.objects.all()
    serializer_class = InscritoSerializer

class InscritoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = inscrito.objects.all()
    serializer_class = InscritoSerializer