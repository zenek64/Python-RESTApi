from django_filters import DateTimeFilter, FilterSet, NumberFilter
from django_filters import rest_framework as filters
from rest_framework import permissions, viewsets

from jedzenie.models import Danie, Restauracja, Szczegoly, Zamowienie
from jedzenie.serializers import (DanieSerializer, RestauracjaSerializer,
                                  SzczegolySerializer, ZamowienieSerializer)


class DanieFilter(FilterSet):
    min_cena = NumberFilter(field_name='Cena', lookup_expr='gte')
    max_cena = NumberFilter(field_name='Cena', lookup_expr='lte')

    class Meta:
        model = Danie
        fields = ['min_cena', 'max_cena']


class DateFilter(FilterSet):
    from_date = DateTimeFilter(field_name="Data", lookup_expr="gte")
    to_date = DateTimeFilter(field_name="Data", lookup_expr="lte")

    class Meta:
        model = Zamowienie
        fields = ["from_date", "to_date"]


class RestauracjaView(viewsets.ModelViewSet):
    queryset = Restauracja.objects.all()

    serializer_class = RestauracjaSerializer
    search_fields = ["Nazwa"]


class DanieView(viewsets.ModelViewSet):
    queryset = Danie.objects.all()

    serializer_class = DanieSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DanieFilter


class ZamowienieView(viewsets.ModelViewSet):
    queryset = Zamowienie.objects.all().order_by("-Data")
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_class = DateFilter
    serializer_class = ZamowienieSerializer
    permission_classes = [permissions.IsAuthenticated]


class SzczegolyView(viewsets.ModelViewSet):
    queryset = Szczegoly.objects.all()

    serializer_class = SzczegolySerializer
    permission_classes = [permissions.IsAuthenticated]
