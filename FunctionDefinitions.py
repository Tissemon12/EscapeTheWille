import time as t

# Värden
tutorial = "ja"
not_played = True
scen1_win = ""
scen2_win = ""
scen2_1_win = ""
scen2_1_1_win = ""
scen2_1_2_win = ""
scen2_2_win = ""
scen2_2_1_win = ""
scen2_2_1_1_win = ""
scen2_2_1_2_win = ""

# Färger
# vit = text som programet skriver, förutom instruktioner (\033[0m)
# röd = död (\033[91m)
# Grön = val och vinst (\033[92m)
# gul = det man skriver (\033[93m)
# blå = skrev fel (\033[94m)


# Denna funktionen välkommnar användaren till spelet
def welcome():
    print("""\033[91m
__________________________________________
            Escape The Wille
""")


# Denna funktion ser om man spelat förut och vill se hur man spelar spelet
def experience(played):
    if played == "ja":
        print("\033[0mok")
        t.sleep(0.5)
        print("Då startar spelet")
        t.sleep(1)
        return False
    elif played == "nej":
        tutorial = input("\033[0mVill du se hur man spelar spelet? (\033[92mja\033[0m/\033[92mnej) \033[93m").lower()
        if tutorial == "nej":
            print("\033[0mok")
            t.sleep(1)
            print("Då startar spelet")
            t.sleep(2)
            return False
        elif tutorial == "ja":
            return tutorial
        else:
            print("\033[94mFörsök igen. Skriv (\033[92mja\033[94m/\033[92mnej)\033[94m tack")
    else:
        print("\033[94mFörsök igen. Skriv (\033[92mja\033[94m/\033[92mnej)\033[94m tack")    


# Funktionen som visar hur man spelar spelet och vidare där ifrån
def instructions(tutorial):
    if tutorial == "nej":
        return
    elif tutorial == "ja" or tutorial == "instruktioner":
        print("""\033[93m
 _______________________________________________
|        Escape The Wille instruktioner         |
|                                               |
| Målet med spelet är att fly från Wille. Man   |
| flyr genom att göra olika val som kommer      |
| presenteras.                                  |
|                                               |
| Vad som kommer hända beror lite på logik      |
| men inte helt. Så försök komma ihåg vad ni    |
| gjort tidigare gånger.                        |
|                                               |
| Om ni vill se denna rutan skriv: instruktioner|
|                                               |
| Om ni vill avsluta spelet skriv: avsluta      |
|                                               |
| Detta är alla instruktioner. Lycka till!      |
|_______________________________________________|
""")
    t.sleep(0)
    done = input("\033[0mLäst färdigt? (\033[92mja\033[0m/\033[92mnej\033[0m) \033[93m")
    if done == "ja":
        print("\033[0mOk")
        t.sleep(1)
        print("Då startar det")
    elif done == "nej":
        print("\033[0mOk. Då kommer rutan igen")
        t.sleep(3)
        return instructions(tutorial)
    else:
        print("\033[94mFörsök igen. Skriv (\033[92mja\033[0m/\033[92mnej\033[94m) tack")
        return instructions(tutorial)


# Denna funktionen visar i slutet av spelet om man dött, överlevt eller lämnat spelet
# Avslutar spelet också
def end(dead):
    if dead == "yes":
        print("\033[91mTyvär, Wille tog dig. Du förlorade")
    elif dead == "no":
        print("\033[92mGrattis! Du flydde från Wille och klarade spelet")
    elif dead == "left":
        print("\033[0mSpelet avslutas")
    exit()


# Funktionen som är introduktionen till spelet
def start():
    print("\033[0mDu är i en fängelse cell")
    t.sleep(2)
    print("Varför?")
    t.sleep(1)
    print("Eftersom du är en tjuv som snor folks donuts")
    t.sleep(3)
    print("Krasch!")
    t.sleep(1.5)
    print("Du krossade ett fönster i cellen")
    t.sleep(2)
    print("När du landar kommer Wille ur utedasset. Han som fängslade dig!")
    t.sleep(3)
    print("Han har en donut som du tar")
    t.sleep(2)
    print("Varför?")
    t.sleep(1)
    print("Du är hungrig. Såklart!")
    t.sleep(2)
    print("Eftersom han är en vakt och du är en fånge så måste du fly!")
    t.sleep(4)
    print("Eftersom du tog hans donut så blir han rasande!")
    t.sleep(3)
    print("Om han tar dig så kommer du försvninna under mystiska omständigheter!")


# Funktionen till ditt första val efter man krossat fönstret på sin cell. Kan välja (vänster/framåt/höger).
def scen1(choice):
    t.sleep(2)
    if choice == "vänster":
        print("\033[0mDu träffar på en hund")
        t.sleep(2)
        print("Den är så ful och äcklig att du svimmar av en schock!")
        t.sleep(2)
        return False
    elif choice == "framåt":
        print("\033[0mDu springer framåt")
        t.sleep(1)
        print("Du hoppar på en en låda och tar sats över stänglset!")
        t.sleep(3)
        print("Precis när du kommer över så fastnar kalsongerna i stängslet")
        t.sleep(3)
        print("Du lyckas inte att komma loss")
        t.sleep(1)
        return False
    elif choice == "höger":
        print("\033[0mDu springer iväg")
        t.sleep(2)
        print("Du hittar en pepsi flaska och ett bandage på ett bord som du tar")
        t.sleep(2)
        choice = input("\033[0mSka du distrahera Wille med pepsi flaskan eller dricka den tills senare? (\033[92mdistrahera\033[0m/\033[92mdricka\033[0m) \033[93m").lower()
        if choice == "dricka":
            print("\033[0mDu dricker den och saktar ner") #inte färdig
            t.sleep(1)
            print("Wille kommer i fatt")
            t.sleep(1)
            return False
        elif choice == "distrahera":
            print("\033[0mDu distraherar Wille och kommer undan") #inte färdig
            t.sleep(1)
            print("Du går en stund och hittar en donut.")
            t.sleep(1)
            return True
        else:
            print("\033[94mFörsök igen. Skriv (\033[92mdricka\033[94m/\033[92mdistrahera\033[94m) tack!")
    else:
        print("\033[94mFörsök igen. Skriv (\033[92mvänster\033[94m/\033[92mframåt\033[94m/\033[92mhöger\033[94m) tack!")


# Funktionen för den andra scenen, det finns en donut på ett bord. Kan välja (äta/lämna/ta).
def scen2(choice):
    t.sleep(2)
    if choice == "äta":
        t.sleep(1)
        print("\033[0mWille blir arg och ringer Khalel för att bomba dig")
        t.sleep(2)
        return False
    elif choice == "lämna":
        print("\033[0mDu går vidare och hittar pengar")
        t.sleep(1)
        return choice
    elif choice == "ta":
        print("\033[0mDu tog saken")
        t.sleep(1)
        print("Wille skjuter ditt ben.")
        t.sleep(1)
        print("Efter ett tag Wille blir trött och kan inte springa längre.")
        t.sleep(2)
        return choice
    else:
        print("\033[94mFörsök igen. Skriv (\033[92mäta\033[94m/\033[92mlämna\033[94m/\033[92mta\033[94m) tack!")


# Funktionen för den tredje scenen om man valde att lämna donuten i scen2. Kan välja (lämna/ta).
def scen2_1(choice):
    t.sleep(1)
    if choice == "lämna":
        print("\033[0mDu går vidare")
        t.sleep(1)
        print("Du hittar ett fönster.")
        t.sleep(1)
        return choice

    elif choice == "ta":
        print("\033[0mDet var en fälla")
        t.sleep(1)
        print("Du skadar ditt ben.")
        t.sleep(1)
        print("Du går vidare och hittar ett fönster")
        t.sleep(1)
        return choice
        
    else:
        print("\033[94mFörsök igen. Skriv (\033[92mlämna\033[94m/\033[92mta\033[94m) tack!")


# Funktionen för den fjärde funktionen om man valde att lämna pengarna i scen2_1. Kan välja (klättra/gå).
def scen2_1_1(choice):
    t.sleep(1)
    if choice == "klättra":
        print("\033[0mDu går ut")
        t.sleep(1)
        return True
    elif choice == "gå":
        print("\033[0mDu går vidare")
        t.sleep(1)
        print("Du hamnar i en återvändsgränd")
        t.sleep(1)
        print("Wille kommer och tar dig")
        t.sleep(1)
        return False
    else:
        print("\033[94mFörsök igen. Skriv (\033[92mklättra\033[94m/\033[92mgå\033[94m) tack!")


# Funktionen för den fjärde funktionen om man valde att ta pengarna i scen2_1. Kan välja (klättra/gå).
def scen2_1_2(choice):
    t.sleep(1)
    if choice == "klättra":
        print("\033[0mDu kan inte klättra eftersom du skada ditt ben")
        t.sleep(2)
        heal = input("\033[0mSka du läka benet med bandaget du fick förut? (\033[92mläka\033[0m/\033[92mklättra\033[0m) \033[93m").lower()
        t.sleep(2)
        if heal == "läka":
            print("\033[0mDu använde bandaget")
            t.sleep(1)
            print("Du klättrar och lyckades")
            t.sleep(1)
            return True

        elif heal == "klättra":
            print("\033[0mDu använde inte bandagt")
            t.sleep(1)
            print("Du försöker klättra om och om igen men misslyckas")
            t.sleep(2)
            return False

        else:
            print("\033[94mFörsök igen. Skriv (\033[92mklättra\033[94m/\033[92mläka\033[92m) tack!")
    
    elif choice == "gå":
        print("\033[0mDu går vidare")
        t.sleep(1)
        print("Men du hammnar istället vid en återvändsgränd")
        t.sleep(1)
        return False
    
    else:
        print("\033[94mFörsök igen. Skriv (\033[92mKlättra\033[94m/\033[92mgå\033[94m) tack!")


# Funktionen för den tredje scenen om man valde att ta donuten i scen2. Kan välja (läka/gå)
def scen2_2(choice):
    t.sleep(1)
    if choice == "läka":
        print("\033[0mDu kan gå igen")
        t.sleep(1)
        print("Du går vidare och hittar pengar")
        t.sleep(1)
        return True
    elif choice == "gå":
        print("\033[0mEfter ett tag ville fångar dig")
        t.sleep(1)
        return False
    
    else: 
        print("\033[94mFörsök igen. Skriv (\033[92mläka\033[94m/\033[92mgå\033[94m) tack")


# Funktionen för den fjärde scenen efter man har läkt sitt ben. kan välja (lämna/ta).
def scen2_2_1(choice):
    t.sleep(1)
    if choice == "lämna":
        print("\033[0mDu går vidare")
        t.sleep(1)
        print("Du hittar ett fönster.")
        t.sleep(1)
        return choice

    elif choice == "ta":
        print("\033[0mDet var en fälla")
        t.sleep(1)
        print("Du skadar ditt ben.")
        t.sleep(1)
        print("Du går vidare och hittar ett fönster")
        t.sleep(1)
        return choice
        
    else:
        print("\033[94mFörsök igen. Skriv (\033[92mlämna\033[94m/\033[92mta\033[94m) tack!")


# Du hittar ett fönster men du är skadad.
def scen2_2_1_1(choice):
    t.sleep(1)
    if choice == "klättra":
        print("\033[0mDu kan inte klättra eftersom du skada ditt ben")
        t.sleep(2)
        heal = input("\033[0mSka du läka benet med bandaget du fick förut? (\033[92mläka\033[0m/\033[92mklättra\033[0m) \033[93m").lower()
        t.sleep(2)
        if heal == "läka":
            print("\033[0mDu använde bandaget")
            t.sleep(1)
            print("Du klättrar och lyckades")
            t.sleep(1)
            return True

        elif heal == "klättra":
            print("\033[0mDu använde inte bandagt")
            t.sleep(1)
            print("Du försöker klättra om och om igen men misslyckas")
            t.sleep(1.5)
            return False

        else:
            print("\033[94mFörsök igen. Skriv (\033[92mklättra\033[94m/\033[92mläka\033[94m) tack!")
    
    elif choice == "gå":
        print("\033[0mDu går vidare")
        t.sleep(1)
        print("Men du hammnar istället vid en återvändsgränd")
        t.sleep(1.5)
        return False
    
    else:
        print("\033[94mFörsök igen. Skriv (\033[92mklättra\033[94m/\033[92mgå\033[94m) tack!")


# Du hittar ett fönster.
def scen2_2_1_2(choice):
    t.sleep(1)
    if choice == "klättra":
        print("\033[0mDu går ut")
        t.sleep(1)
        return True
    elif choice == "gå":
        print("\033[0mDu går vidare")
        t.sleep(1)
        print("Du hamnar i en återvändsgränd")
        t.sleep(1.1)
        return False
    else:
        print("\033[94mFörsök igen. Skriv (\033[92mklättra\033[94m/\033[92mgå\033[94m) tack!")
