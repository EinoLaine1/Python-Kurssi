import random

maara = int(input("Montako noppaa?: "))

summa = 0

for i in range(maara):
    heitto = random.randint(1,6)
    print("Heitto:", heitto)
    summa += heitto

print("Silmälukujen summa on:", summa)
