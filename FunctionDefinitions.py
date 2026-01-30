import time as t


# Denna funktionen välkommnar användaren till spelet
def welcome():
    print("""
__________________________________________
            Escape The Wille
""")


# Denna funktion ser om man spelat förut och vill se hur man spelar spelet
def experience():
    played = input("Spelat förrut (ja/nej)? ").lower()
    if played == "ja":
        print("ok")
        t.sleep(0.5)
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


