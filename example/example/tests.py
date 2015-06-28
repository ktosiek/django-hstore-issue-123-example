from django.test import TestCase

from .fields import Hand
from .models import HandInHStore


def hand_factory():
    return Hand(
        [n + 's' for n in 'A23456789TJQK'],
        [n + 'h' for n in 'A23456789TJQK'],
        [n + 'c' for n in 'A23456789TJQK'],
        [n + 'd' for n in 'A23456789TJQK'],
    )
        


class HandInHStoreTestCase(TestCase):
    def test_writing_and_reading_a_hand(self):
        instance = HandInHStore()
        hand = Hand(['2s', '3s'], ['2h', '3h'], ['2c', '3c'], ['2d', '3d'])

        instance.hand = hand
        instance.save()
        instance.refresh_from_db()

        self.assertEqual(hand, instance.hand)
