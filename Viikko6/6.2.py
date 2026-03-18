import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

maksimi = int(input("Anna nopan maksimi silmäluku: "))

while True:
    tulos = heita_noppaa(maksimi)
    print(tulos)
    if tulos == maksimi:
        break