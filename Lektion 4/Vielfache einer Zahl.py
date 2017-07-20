# Vielfache einer Zahl

print("\n***************************************************************\n")

while True:
    Zahl = int(input("Gib eine Zahl ein von der du die Vielfachen haben willst: "))

    i = 0

    for i in range(1, 11):
        Hulu = Zahl * i
        print(i, "*", Zahl, "=", Hulu)

    antwort = input('\nWillst du noch ein anderes Vielfaches einer Zahl haben dann gib ein: "Nochmal" ansonsten Drücke die Entertaste\n\"Nochmal" oder Enter:')

    print("\n***************************************************************\n")

    if antwort != "Nochmal":
        break


