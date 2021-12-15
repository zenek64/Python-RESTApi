from django.db import models


class Restauracja(models.Model):
    idRestauracja = models.AutoField(primary_key=True, unique=True)
    Nazwa = models.CharField(max_length=45, unique=True)
    Adres = models.CharField(max_length=45)
    Rodzaj_dan = models.CharField(max_length=45)
    Cena_dostawy = models.FloatField(max_length=12)
    Kategoria = models.CharField(max_length=45, blank=True)

    def __str__(self):
        return self.Nazwa


class Danie(models.Model):
    idDanie = models.AutoField(primary_key=True, unique=True)
    idRestauracja = models.ForeignKey(Restauracja, on_delete=models.CASCADE)
    Nazwa = models.CharField(max_length=45)
    Rodzaj = models.CharField(max_length=45)
    Cena = models.FloatField(max_length=45)

    def __str__(self):
        return self.Nazwa


class Zamowienie(models.Model):
    idZamowienie = models.AutoField(primary_key=True, unique=True)
    Imie = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    Adres = models.CharField(max_length=45)
    Telefon = models.CharField(max_length=45)
    Email = models.CharField(max_length=45)
    Data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Adres


class Szczegoly(models.Model):
    Ilosc = models.IntegerField()
    Cena = models.FloatField(max_length=45)
    Zamowienie_idZamowienie = models.ForeignKey(Zamowienie,
                                                on_delete=models.CASCADE)
    Danie_idDanie = models.ForeignKey(Danie, on_delete=models.CASCADE)
