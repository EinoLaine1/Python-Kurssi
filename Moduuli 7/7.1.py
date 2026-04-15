vuodenajat = {
    "talvi": [12, 1, 2],
    "kevät": [3, 4, 5],
    "kesä": [6, 7, 8],
    "syksy": [9, 10, 11]
}

kk = int(input("Anna kuukauden numero (1-12): "))

# Tarkistetaan vuodenaika
for vuodenaika, kuukaudet in vuodenajat.items():
    if kk in kuukaudet:
        print(f"Vuodenaika on {vuodenaika}.")
        break
else:
    print("Virheellinen kuukausi.")