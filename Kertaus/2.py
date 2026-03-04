tunnit = int(input("Anna tunnit:"))
tuntipalkka = int(input("Anna palkka: "))
paiva = input("Anna viikonpaiva: ")

if paiva == "sunnuntai":
    tuntipalkka = 2 * tuntipalkka

paivapalkka = tunnit * tuntipalkka
print("Palkka on", paivapalkka)