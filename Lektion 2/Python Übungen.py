Jahr = int(input("In welchem Jahr bist du geboren? : "))

Monat = int(input("In welchem Monat (als Zahl) hast du Geburtstag? : "))

Tag = int(input("An Welchem Tag hast du Geburtstag? : "))

Alter = 2017 - Jahr

##if Monat < 7:
##  print ("Du hattest schon Geburtstag! Du bist", Alter, "Jahre alt!")  
##elif Monat > 7:
##    print ("Du wirst dieses Jahr noch", Alter, "Jahre Alt!")
##elif Monat == 7 and Tag < 19:
##    print ("Du hattest diesen Monat Geburtstag und wurdest", Alter, "Jahre Alt!")
##elif Monat ==7 and Tag > 19:
##    print ("Du wirst diesen Monat noch Geburtstag habe und wirst dann", Alter, "Jahre Alt!")
##elif Tag== 19 and Monat == 7:
##    print("Alles Gute zum Geburtstag :D ! Du wurdest ", Alter ," Jahre alt!")
    
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
