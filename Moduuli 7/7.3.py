lentoasemat = {}

while True:
    toiminto = input(
        "\nValitse toiminto:\n"
        "1 = Lisää lentoasema\n"
        "2 = Hae lentoasema\n"
        "3 = Lopeta\n"
        "Valinta: "
    )

    if toiminto == "1":
        icao = input("Anna ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema lisätty.")

    elif toiminto == "2":
        icao = input("Anna ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"Lentoaseman nimi: {lentoasemat[icao]}")
        else:
            print("Lentoasemaa ei löytynyt.")

    elif toiminto == "3":
        print("Ohjelma lopetettu.")
        break

    else:
        print("Virheellinen valinta.")