Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print ("Hello world!")
Hello world!
>>> print ("Dei Mudda"*5)
Dei MuddaDei MuddaDei MuddaDei MuddaDei Mudda
>>> print ("hallo"+"welt")
hallowelt
>>> print (3*7)
21
>>> 3*7
21
>>> 7 ** 1990
55603179789325970611925220018440346019546109364386330681602635841783846514337051490472358421173899734511258761505984038168959616141989070606829343934608360404574423675051132030651107411873766918301561251886620271717972915020812861945997645053771171383606366995823439599433387638685985767892194882610077879962531403607170520673740007618399561391131391924150343055278427902210154649676098921342921606359364160904467401282216336526009498473694416819984312271882564885358658802278444440366631620382191756940157460457065010657781717671571329020131587138998266595452220770190647150054444533662061328000143282657038588954071921936532767216899018676100919750043886143844148061042144553014622982747924598736528005105744549705667464345061723985646440576253146181099058567962631946384029265282208753721212488945140323537734132155758440135009919270986855675397109217963196880462106039268271221418435357194113102424818859131756420042529815014794632530742377614909198434467179743630878327810315915076864756704454527855535216723189383272477565451634601886932169481761794324964994500090401545451034864136438867562662176167837175217987681427897558063857927985130579076324595416626205536146264731047780808776042940644594562721921874406851799787963807306125750132003503984554347486594957276329368205020877626597975451169162623090709100942238557498180867730932503518235678115455406107919151079219697246166122534233531297501184494879863564208141775755255313365749445611367781784653341845383850658865557189810537334242332861207530620187276438717538984091907031587617161529292287259097700127507803190812872716216445275467265991050978066111416903508975444879444098504421468196488353782273069816046071887249
>>> 7 //4
1
>>> 7 / 4
1.75
>>> 7%4
3
>>> pi
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    pi
NameError: name 'pi' is not defined
>>> print ("Hallo", "Welt", 1724)
Hallo Welt 1724
>>> 7*3 == 20+1
True
>>> 7+3 < 9+2
True
>>> 7** 5 >10**3
True
>>> 7+2 != 8+1
False
>>> 7>= 5
True
>>> 7<=5
False
>>> print ("hallo" *3, sep="-")
hallohallohallo
>>> print ("hallo", "hallo", "hallo" sep="-")
SyntaxError: invalid syntax
>>> print ("hallo", "hallo", "hallo", sep="-")
hallo-hallo-hallo
>>> print ("hallo-" *3)
hallo-hallo-hallo-
>>> print ("Ich frage: \"Wie ist das Wetter heute?\"")
Ich frage: "Wie ist das Wetter heute?"
>>> print ('Ich frage: "Wie wird das Wetter heute?")
       
SyntaxError: EOL while scanning string literal
>>> print ('Ich frage: "Wie wird das Wetter heute?"')
Ich frage: "Wie wird das Wetter heute?"
>>> name="Simon"
>>> nachname="Bender"
>>> print (name, nachname)
Simon Bender
>>> Gesamter_name=name+nachname
>>> print (gesamter_name)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print (gesamter_name)
NameError: name 'gesamter_name' is not defined
>>> print (Gesamter_name)
SimonBender
>>> z1=1
>>> z1
1
>>> zahl1= 2.0
>>> print(zahl1-z1)
1.0
>>> geldmenge=1404
>>> print ("Ich habe", str(geldmenge) + "€", "auf dem Konto!")
Ich habe 1404€ auf dem Konto!
>>> zahl=17
>>> print(int(zahl) +3)
20
>>> print("Robin hat", str(float("17") +3) + "€", "auf dem Konto!")
Robin hat 20.0€ auf dem Konto!
>>> round (5.7)
6
>>> name= input("Geben Sie ihren Namen ein: ")
Geben Sie ihren Namen ein: Simon
>>> print(name)
Simon
>>> eingabe=input()
Simon
>>> eingabe
'Simon'
>>> name="Simon"
>>> nachname="Bender"
>>> name = name+ nachname
>>> name
'SimonBender'
>>> name ="Simon"
>>> name +=" "
>>> name+= nachname
>>> name
'Simon Bender'
>>> versuche=7
>>> leben=2
>>> leben-=1
>>> leben
1
>>> leben-=1
>>> leben
0
>>> print("Du hast verloren, du Opfer!")
Du hast verloren, du Opfer!
>>> eingabe= input("Neuer Versuch? (yes/no)"))
SyntaxError: invalid syntax
>>> eingabe= input("Neuer Versuch? (yes/no)")
Neuer Versuch? (yes/no)yes
>>> name= "Simon"
>>> name += ' '
>>> 
