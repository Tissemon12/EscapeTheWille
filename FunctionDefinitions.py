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
        tutorial = input("Vill du se hur man spelar spelet (ja/nej)?").lower()
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


def scen1(choice):
    if choice == "vänster":
        print("Du träffar på en hund")
        t.sleep(2)
        print("Den är så ful och äcklig att du dör av en hjärtattack!")
        return True
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
            print("du dricker den, wille tar dig, du förlorar") #inte färdig
            return False
        elif choice == "distrahera":
            print("du distraherar Wille och kommer undan") #inte färdig
            return True
        else:
            print("Försök igen. Skriv (dricka/distrahera) tack!")
    else:
        print("Försök igen. Skriv (vänster/framåt/höger) tack!")