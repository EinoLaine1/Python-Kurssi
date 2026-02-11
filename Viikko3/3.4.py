vuosiluku = int(input("Vuosiluku: "))
if vuosiluku % 4 == 0 or vuosiluku % 100 and vuosiluku % 400 == 0:
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")