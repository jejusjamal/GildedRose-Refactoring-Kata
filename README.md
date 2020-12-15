#GildedRose-Refactoring-Kata

# python solution for GildedRose-Refactoring-Kata

#We can just add few lines of code as below to original code to achive what we needed to support "Conjured Mana Cake".
```
   def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" \
                    and item.name != "Backstage passes to a TAFKAL80ETC concert" \
                    and item.name != "Conjured Mana Cake":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1

            elif item.name == "Conjured Mana Cake":
                if 0 < item.quality < 50:
                    item.quality = item.quality - 2
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11: 
```


but still this solution is not very efficient and doest not improve the code quality and we will still face challenges modifying and undertanding this code in future if any changes needed.
To overcome this I had to refactor the code to make it readable and easy to understand for anyone if any new feature needs to be added. I have broken the complex if else nested logic into simple methods based on the various product category that we dealing with, this makes it modular and will help anyone to easily change it in future.

Also to test the scenarios added unit test cases of every condition that we need to vailidate 

# Steps To Test:


1) ```python test_gilded_rose.py``` (this will cover all the unit test cases that we need to vailidate)
2) ```python texttest_fixture.py <days>``` (this will cover the fixed test data we need to verify the outputs manually based on inputs we provided. if you dont pass days it will take 2 days as default)
