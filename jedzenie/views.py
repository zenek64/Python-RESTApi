from django.shortcuts import render
from rest_framework import viewsets

from jedzenie.models import Restauracja, Danie, Zamowienie, Szczegoly
from jedzenie.serializers import RestauracjaSerializer, DanieSerializer, ZamowienieSerializer, SzczegolySerializer


class RestauracjaView(viewsets.ModelViewSet):
    queryset = Restauracja.objects.all()

    serializer_class = RestauracjaSerializer

class DanieView(viewsets.ModelViewSet):
    queryset = Danie.objects.all()

    serializer_class = DanieSerializer

class ZamowienieView(viewsets.ModelViewSet):
    queryset = Zamowienie.objects.all()

    serializer_class = ZamowienieSerializer

class SzczegolyView(viewsets.ModelViewSet):
    queryset = Szczegoly.objects.all()

    serializer_class = SzczegolySerializer




