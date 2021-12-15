# -*- coding: utf-8 -*-

"""Tests for models."""
# Django
from django.db.models import signals
from django.test import TestCase

# 3rd-party
import factory.fuzzy
# Local
from jedzenie.tests.factories import RestauracjaFactory, ZamowienieFactory


class TestModels(TestCase):
    """Test models."""

    @factory.django.mute_signals(signals.post_save)
    def test_Restauracja(self):
        """Test restauracji."""
        my_model = RestauracjaFactory()
        my_model2 = RestauracjaFactory()

        # self.assertEqual(f'{my_model.Kategoria}', "Pizza")
        self.assertEqual(f'{my_model.Nazwa}', str(my_model))
        self.assertEqual(f'{my_model.Nazwa}', "Nazwa 0")
        self.assertEqual(f'{my_model.idRestauracja}', "1")
        self.assertEqual(f'{my_model2.Nazwa}', "Nazwa 1")
        self.assertEqual(f'{my_model2.idRestauracja}', "2")

    @factory.django.mute_signals(signals.post_save)
    def test_Zamowienie(self):
        """Test zamówień."""
        my_model = ZamowienieFactory()
        my_model2 = ZamowienieFactory()

        self.assertEqual(f'{my_model.Adres}', str(my_model))
        self.assertEqual(f'{my_model.Adres}', "Adres 0")
        self.assertEqual(f'{my_model2.Adres}', "Adres 1")
