luvut = []

while True:
    syote = input("Anna luku: ")

    if syote == "":
        break

    luku = float(syote)
    luvut.append(luku)

if len(luvut) > 0:
    print(f"Pienin luku: {min(luvut)}")
    print(f"Suurin luku: {max(luvut)}")
else:
    print("Et antanut yhtään lukua.")