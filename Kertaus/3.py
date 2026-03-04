import math

while True:
    luku = int(input("Anna kokonaisluku: "))

    if luku == 0:
        print("Ohjelma päättyy.")
        break

    if luku < 0:
        print("Virheellinen numero")
    elif luku > 0:
        neliojuuri = math.sqrt(luku)
        print(f"Luvun neliöjuuri on {neliojuuri}")
    else:
        print("Luku on nolla, neliöjuuri on 0.0")

    print("-" * 20)
