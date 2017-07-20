a = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]

while True:
    Jahr = int(input("In welchem Jahr bist du geboren?: "))

    Monat = (input("In welchem Monat hast du Geburtstag? (Achte auf Groß und Kleinschreibung): "))

    Tag = int(input("An Welchem Tag hast du Geburtstag?: "))

    Alter = 2017 - Jahr

    print("\n####################\n")

    Monat = a.index(Monat) +1

        
    if Monat < 7:

        print("Du hattest schon Geburtstag! Du bist", Alter, "Jahre alt!")


    elif Monat == 7:

        if Tag < 19:
            print("Du hattest schon Geburtstag! Du bist", Alter, "Jahre alt!")

        elif Tag == 19:
            print("Alles Gute zum Geburtstag :D ! Du wurdest ", Alter ," Jahre alt!")

        elif Tag > 19:
            print("Du wirst diesen Monat noch Geburtstag haben und wirst dann", Alter,"Jahre alt!")


    elif Monat > 7:
        print ("Du wirst dieses Jahr noch Geburtstag haben und wirst dann", Alter,"Jahre Alt!")


    antwort = input("\nWollen Sie noch einmal Ihr Alter Überprüfen? Wenn Sie nochmal ihr Alter überprüfen wollen geben sie Ich will nochmal!! ein ansonsten drücken sie die Entertaste ein!\n\nIch will nochmal!! oder Enter:")


    if antwort != "Ich will nochmal!!":
        break

    else:
        print("\n####################\n")
