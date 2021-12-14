from django_filters import FilterSet, NumberFilter
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
    queryset = Zamowienie.objects.all().order_by("-Data")
    # filter = DateFilter
    serializer_class = ZamowienieSerializer


class SzczegolyView(viewsets.ModelViewSet):
    queryset = Szczegoly.objects.all()

    serializer_class = SzczegolySerializer


class DanieFilter(FilterSet):
    min_cena = NumberFilter(field_name='Cena', lookup_expr='gte')
    max_cena = NumberFilter(field_name='Cena', lookup_expr='lte')

    class Meta:
        model = Danie
        fields = ['min_cena', 'max_cena']
