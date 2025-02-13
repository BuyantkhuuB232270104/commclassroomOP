class GroceryStore:
    def __init__(uu, name, apple_zaragdsan_kg, apple_une, orange_zaragdsan_kg, orange_une):
        uu.name = name
        uu.apple_zaragdsan_kg = apple_zaragdsan_kg
        uu.apple_une = apple_une
        uu.orange_zaragdsan_kg = orange_zaragdsan_kg
        uu.orange_une = orange_une

    def calculate_butsaalt(uu):
        apple_butsaalt = uu.apple_zaragdsan_kg * uu.apple_une
        orange_butsaalt = uu.orange_zaragdsan_kg * uu.orange_une
        return apple_butsaalt + orange_butsaalt



bambaruush = GroceryStore("Bambaruush", 534, 5000, 487, 10000)
jimshen = GroceryStore("Jimshen", 764, 4800, 423, 9300)
fruits = GroceryStore("Fruits", 136, 5000, 228, 10000)


bambaruush_butsaalt = bambaruush.calculate_butsaalt()
jimshen_butsaalt = jimshen.calculate_butsaalt()
fruits_butsaalt = fruits.calculate_butsaalt()


print(f"Bambaruush дэлгүүрийн орлого: {bambaruush_butsaalt}")
print(f"Jimshen дэлгүүрийн орлого: {jimshen_butsaalt}")
print(f"Fruits дэлгүүрийн орлого: {fruits_butsaalt}")


niit_butsaalt = bambaruush_butsaalt + jimshen_butsaalt + fruits_butsaalt
print(f"Нийт дэлгүүрийн орлого: {niit_butsaalt}")