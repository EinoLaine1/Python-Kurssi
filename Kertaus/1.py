keitto = 5.9
nimi = input('Anna nimesi:')
if nimi == "pena":
    print("Seuraava, kiitos!")
else:
    nakki = int(input("Montako keittoannosta? "))
    hinta = nakki * keitto
    print("Kokonaishinta on", hinta, "euroa")
