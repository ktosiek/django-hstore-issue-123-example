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
    def test_writing_and_reading_a_hand_with_hstore(self):
        instance = HandInHStore()
        hand = hand_factory()

        instance.hand = hand
        instance.save()
        instance.refresh_from_db()

        self.assertEqual(hand, instance.hand)

    def test_writing_and_reading_a_native_hand(self):
        instance = HandInHStore()
        hand = hand_factory()

        instance.native_hand = hand
        instance.save()
        instance.refresh_from_db()

        self.assertEqual(hand, instance.native_hand)
