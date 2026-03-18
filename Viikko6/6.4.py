
def laske_summa(lukulista):
    summa = 0
    for luku in lukulista:
        summa += luku
    return summa

def main():

    numerot = [10, 20, 30, 40, 50]

    tulos = laske_summa(numerot)

    print(f"Listan {numerot} summa on: {tulos}")

if __name__ == "__main__":
    main()