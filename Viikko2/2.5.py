leiviskat = int(input("Anna leiviskat: "))
naulat = int(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

luoti = 13.3
naula = 425.6
leiviska = 8512

kokonaisgrammat = (
    leiviskat * leiviska +
    naulat * naula +
    luodit * luoti
)

kilogrammat = int(kokonaisgrammat // 1000)
grammat = kokonaisgrammat - kilogrammat * 1000

print("Massa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")