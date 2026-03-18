
def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

while True:
    maara = float(input("Anna bensiinimäärä gallonoina (negatiivinen lopettaa): "))

    if maara < 0:
        break

    litrat = gallonat_litroiksi(maara)
    print(f"{litrat:.3f} litraa")