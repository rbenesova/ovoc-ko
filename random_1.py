import random
ovoce = ["jahoda", "jablko", "malina", "boruvka", "citron", "liči"]
i  = ()
for i in range(10):
    osoba1 = random.choice(ovoce)
    osoba2 = random.choice(ovoce)
    print(f"kupme {osoba1}")
    if osoba1 == osoba2:
        jinaMoznost = random.choice(ovoce)
        print(f"ne kupme {jinaMoznost}")
    else:
        print(f"ne kupme {osoba2}")