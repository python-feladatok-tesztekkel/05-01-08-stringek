from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestLegrovidebbSzo(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.szavak_szama("Készül Julcsi főzni húsz ember számára")
        elvart = 4
        self.assertEqual(elvart, aktualis, "Nem jól határozta mega szavak számát")
    def test_feladat02(self):
        aktualis = feladatok.szavak_szama("Megerősítették állásaikat pedig ellenség nem volt.")
        elvart = 3
        self.assertEqual(elvart, aktualis, "Nem jól határozta mega szavak számát")
    def test_feladat03(self):
        aktualis = feladatok.szavak_szama("aaaa bbbbbbbbbb cccccccccccccccc ddddddddd eeeeee")
        elvart = 4
        self.assertEqual(elvart, aktualis, "Nem jól határozta mega szavak számát")
    def test_feladat04(self):
        aktualis = feladatok.szavak_szama("bbbbbbbbbb cccccccccccccccc ddddddddd eeeeee aa")
        elvart = 2
        self.assertEqual(elvart, aktualis, "Nem jól határozta mega szavak számát")
    def test_feladat05(self):
        aktualis = feladatok.szavak_szama("333 333 333 333 333 333 333 333 333 333 333 333 333 333 333 333 333 333 333 333 333")
        elvart = 3
        self.assertEqual(elvart, aktualis, "Nem jól határozta mega szavak számát")
    def test_feladat06(self):
        aktualis = feladatok.szavak_szama("1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1")
        elvart = 1
        self.assertEqual(elvart, aktualis, "Nem jól határozta mega szavak számát")
    def test_feladat08(self):
        aktualis = feladatok.szavak_szama("")
        elvart = 0
        self.assertEqual(elvart, aktualis, "Nem jól határozta mega szavak számát")


