# -*- coding: utf-8 -*-

import factory.fuzzy
from faker import Faker
from jedzenie.models import Restauracja, Zamowienie

faker = Faker('pl_PL')


class RestauracjaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Restauracja

    Nazwa = factory.Sequence(lambda n: f'Nazwa {n}')
    Adres = factory.Sequence(lambda n: f'Adres {n}')
    Rodzaj_dan = factory.Sequence(lambda n: f'Rodzaj {n}')
    Cena_dostawy = factory.Sequence(lambda n: n)
    Kategoria = factory.fuzzy.FuzzyChoice([
        'Pizza',
        'Kebab',
        'Azjatycka',
        'Chińska',
        'Polska',
        'Włoska',
    ])


class ZamowienieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Zamowienie

    Imie = factory.Sequence(lambda n: f'Imie {n}')
    Nazwisko = factory.Sequence(lambda n: f'Nazwisko {n}')
    Adres = factory.Sequence(lambda n: f'Adres {n}')
    Telefon = faker.phone_number()
    Email = factory.Sequence(lambda n: f'Email {n}')
    Data = faker.date()
