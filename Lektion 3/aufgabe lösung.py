    # Addierer +1

print("Dies ist ein Addierer")

zahl1 = int(input("Zahl 1: "))
zahl2 = int(input("Zahl 2: "))

addierungszahl = 0

print(zahl1)

while addierungszahl < zahl2:

    addierungszahl += 1
    zahl1 += 1

    print(zahl1)
    if addierungszahl == zahl2:
        break

ergebnis = zahl1


print("Ergebnis:", ergebnis)
