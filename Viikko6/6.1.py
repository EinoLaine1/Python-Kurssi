def karsi_parittomat(alkuperainen_lista):
    parilliset = []
    for luku in alkuperainen_lista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset


def main():
    testilista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu_lista = karsi_parittomat(testilista)

    print(f"Alkuperäinen lista: {testilista}")
    print(f"Karsittu lista: {karsittu_lista}")


if __name__ == "__main__":
    main()