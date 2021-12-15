from rest_framework import serializers

from .models import Danie, Restauracja, Szczegoly, Zamowienie


class RestauracjaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restauracja
        fields = ["Nazwa", "Adres", "Rodzaj_dan", "Cena_dostawy", "Kategoria"]


class DanieSerializer(serializers.ModelSerializer):

    class Meta:

        model = Danie
        fields = ["idRestauracja", "Nazwa", "Rodzaj", "Cena"]


class ZamowienieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zamowienie
        fields = ["Imie", "Nazwisko", "Adres", "Telefon", "Email", "Data"]


class SzczegolySerializer(serializers.ModelSerializer):

    class Meta:

        model = Szczegoly
        fields = ["Ilosc", "Cena", "Zamowienie_idZamowienie", "Danie_idDanie"]
