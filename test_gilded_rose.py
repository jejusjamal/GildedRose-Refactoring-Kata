# -*- coding: utf-8 -*-
import unittest
from gilded_rose import GildedRose
from item_factory import ItemFactory

item_factory = ItemFactory()

class GildedRoseTest(unittest.TestCase):
    def test_regular_quality(self):
        items = [item_factory.create("bread", 20, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].quality)

    def test_regular_sell_in(self):
        items = [item_factory.create("bread", 24, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].sell_in)

    def test_regular_sell_in_passed(self):
        items = [item_factory.create("bread", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(38, items[0].quality)

    def test_regular_sell_in_negative(self):
        items = [item_factory.create("bread", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)

    def test_regular_quality_negative(self):
        items = [item_factory.create("bread", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_agedbrie_quality(self):
        items = [item_factory.create("Aged Brie", 10, 8)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)

    def test_agedbrie_sell_in(self):
        items = [item_factory.create("Aged Brie", 12, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].sell_in)

    def test_agedbrie_quality_exceeded(self):
        items = [item_factory.create("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_quality_unchanged(self):
        items = [item_factory.create("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_sell_in_unchanged(self):
        items = [item_factory.create("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)

    def test_backstage_quality(self):
        items = [item_factory.create("Backstage passes to a TAFKAL80ETC concert", 15, 33)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(34, items[0].quality)

    def test_backstage_quality_double_increase(self):
        items = [item_factory.create("Backstage passes to a TAFKAL80ETC concert", 9, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_backstage_quality_triple_increase(self):
        items = [item_factory.create("Backstage passes to a TAFKAL80ETC concert", 2, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(33, items[0].quality)

    def test_backstage_quality_expires(self):
        items = [item_factory.create("Backstage passes to a TAFKAL80ETC concert", -1, 48)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_quality_exceeded(self):
        items = [item_factory.create("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_backstage_sell_in(self):
        items = [item_factory.create("Backstage passes to a TAFKAL80ETC concert", 6, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].sell_in)

    def test_conjured_quality(self):
        items = [item_factory.create("Conjured Mana Cake", 6, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)

    def test_conjured_sell_in(self):
        items = [item_factory.create("Conjured Mana Cake", 5, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)


if __name__ == '__main__':
    unittest.main()
