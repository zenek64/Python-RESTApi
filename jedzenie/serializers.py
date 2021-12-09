from rest_framework import serializers
from .models import Restauracja, Danie, Zamowienie, Szczegoly


class RestauracjaSerializer(serializers.ModelSerializer):

    class Meta:
        model=Restauracja
        fields=["Nazwa", "Adres", "Rodzaj_dan","Cena_dostawy","Kategoria"]

    # def create(self, validated_data):
    #     return Restauracja.objects.create(validated_data)

    def to_representation(self, instance):
        return instance.Nazwa


class DanieSerializer(serializers.ModelSerializer):

    class Meta:
        model=Danie
        fields=["Nazwa", "Rodzaj", "Cena"]

    def to_representation(self, instance):
        return instance.Nazwa

class ZamowienieSerializer(serializers.ModelSerializer):

    class Meta:
        model=Zamowienie
        fields=["Imie", "Nazwisko", "Adres", "Telefon", "Email", "Data"]

    def to_representation(self, instance):
        return instance.Adres

class SzczegolySerializer(serializers.ModelSerializer):

    class Meta:
        model=Szczegoly
        fields=["Ilosc","Cena"]

    def to_representation(self, instance):
        return instance.Cena