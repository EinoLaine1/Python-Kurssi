sukupuoli = input("sukupuoli: ")
hemoglobiini = int(input("hemoglobiini: "))
if sukupuoli == "nainen":
   if hemoglobiini < 117:
       print("Hemoglobiini on alhainen")
   elif hemoglobiini > 175:
       print("Hemoglobiini on korkea")
   else:
       print("Hemoglobiini on normaali")
if sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiini on alhainen")
    elif hemoglobiini > 195:
        print("Hemoglobiini on korkea")
    else:
        print("Hemoglobiini on normaali")