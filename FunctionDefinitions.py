import time as t


# Denna funktionen välkommnar användaren till spelet
def welcome():
    print("""
__________________________________________
            Escape The Wille
""")


# Denna funktion ser om man spelat förut och vill se hur man spelar spelet
def experience(played):
    if played == "ja":
        print("ok")
        t.sleep(0.5)
        tutorial = input("Vill du se hur man spelar spelet (ja/nej)? ").lower()
        if tutorial == "nej":
            print("ok")
            t.sleep(1)
            print("Då startar spelet")
            return
        elif tutorial == "ja":
            return tutorial
        else:
            print("Försök igen. Skriv ja/nej tack")
    elif played == "nej":
        tutorial = input("Vill du se hur man spelar spelet (ja/nej)? ").lower()
        if tutorial == "nej":
            print("ok")
            t.sleep(1)
            print("Då startar spelet")
            return
        elif tutorial == "ja":
            return tutorial
        else:
            print("Försök igen. Skriv ja/nej tack")
    else:
        print("Försök igen. Skriva ja/nej tack")    


# Funktionen som visar hur man spelar spelet och vidare där ifrån
def instructions(tutorial):
    if tutorial == "nej":
        return
    elif tutorial == "ja" or tutorial == "instruktioner":
        print("""
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
    done = input("Läst färdigt? (ja/nej) ")
    if done == "ja":
        done_extra = input("Säker? (ja/nej) ")
        if done_extra == "ja":
            print("Ok")
            t.sleep(1)
            print("Då startar det")
        elif done_extra == "nej":
            print("Ok. Då kommer rutan igen")
            t.sleep(3)
            return instructions(tutorial = "ja")
        else:
            print("Försök igen. Skriv ja/nej tack")
    elif done == "nej":
        print("Ok. Då kommer rutan igen")
        t.sleep(3)
        return instructions(tutorial = "ja")
    else:
        print("Försök igen. Skriv ja/nej tack")


# Denna funktionen visar i slutet av spelet om man dött, överlevt eller lämnat spelet
def end(dead):
    if dead == "yes":
        print("Tyvär, Wille tog dig. Du förlorade")
    elif dead == "no":
        print("Grattis! Du flydde från Wille och klarade spelet")
    elif dead == "left":
        print("Spelet avslutas")


# Funktionen som är introduktionen till spelet
def start():
    print("Du är i en fängelse cell")
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


# Funktionen till din första choice
def scen1(choice):
    if choice == "vänster":
        print("Du träffar på en hund")
        t.sleep(2)
        print("Den är så ful och äcklig att du dör av en hjärtattack!")
        return False
    elif choice == "framåt":
        print("Du springer framåt")
        t.sleep(1)
        print("Du hoppar på en en låda och tar sats över stänglset!")
        t.sleep(3)
        print("Precis när du kommer över så fastnar kalsongerna i stängslet")
        t.sleep(3)
        print("Du kommer inte loss och Wille hinner ta dig")
        return False
    elif choice == "höger":
        print("Du springer iväg")
        t.sleep(2)
        print("Du hittar en pepsi flaska och ett bandage på ett bord som du tar")
        t.sleep(0)
        choice = input("Ska du distrahera Wille med pepsi flaskan eller dricka den tills senare (distrahera/dricka)").lower()
        if choice == "dricka":
            print("du dricker den, wille tar på dig, du förlorar") #inte färdig
            return False
        elif choice == "distrahera":
            print("du distraherar Wille och kommer undan") #inte färdig
            print("Du går en stund och hittar en donut.")
            return True
        else:
            print("Försök igen. Skriv (dricka/distrahera) tack!")
    else:
        print("Försök igen. Skriv (vänster/framåt/höger) tack!")

    
def scen2(choice):
    t.time(0)
    
    if choice == "Äta":
        t.sleep(0)
        print("Wille blir arg och ringer Khalel för att bomba dig")
        return False
    elif choice == "lämna":
        print("Du går vidare och hittar pengar")
        return True
    elif choice == "ta":
        print("du tog saken")
        t.sleep(0)
        print("Wille skjuter ditt ben.")
        t.sleep(0)
        print("Efter ett tag Wille blir trött och kan inte springa längre.")
        return True
    else:
        print("Försök igen")


def scen3(choice):
    if choice == "lämna":
        print("Du går vidare")
        t.sleep(0)
        print("Du hittar ett fönster.")
        t.sleep(0)
        lastChoice1 = input("Klättra/Stanna").lower()
        if lastChoice1 == "klättra":
            print("Du går ut")
            t.sleep(0)
            print("Du vann")
            return True
        else:
            print("Du förlora")
            return False

    elif choice == "ta":
        print("Det var en fälla")
        t.sleep(0)
        print("Du skadar ditt ben.")
        t.sleep(0)
        print("Du går vidare och hittar ett fönster")
        t.sleep(0)
        lastChoice2 = input("Klättra/Stanna").lower()
        if lastChoice2 == "klättra":
            print("Du kan inte klättra eftersom du skada ditt ben")
            t.sleep(0)
            heal = input("Heal/DontHeal").lower()
            if heal == "heal":
                print("Du använde bandage.")
                t.sleep(0)
                print("Du klättrar")
                t.sleep(0)
                print("Du vann")
                return True
            
            else:
                print("Du använde inte bandage.")
                t.sleep(0)
                print("Wille tar på dig")
                t.sleep(0)
                print("Game over")
        
        
        
    
    else:
        print("Försök igen")


def scen4(choice):
    t.sleep(0)
    print("Wille blir trött och kan inte springa längre.")
    t.sleep(0)
    heal = input("Vill du läka ditt ben? Nej/Ja").lower()
    if heal == "nej":
        print("Efter ett tag ville fångar dig")
        t.sleep(0)
        return False
    elif heal == "ja":
        print("Du kan gå igen")
        return True
    
    else: 
        print("Försök igen, din jävla khanzir")


