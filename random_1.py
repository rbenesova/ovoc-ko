import random
ovoce = ["jahoda", "jablko", "malina", "boruvka", "citron", "liči"]
i  = ()
for i in range(10):
    osoba1 = random.choice(ovoce)
    osoba2 = random.choice(ovoce)
    print(f"kupme {osoba1}")
    if osoba1 == osoba2:
        print(f"ne kupme jinou vec")
    else:
        print(f"ne kupme {osoba2}")