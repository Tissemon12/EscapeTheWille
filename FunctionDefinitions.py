import time as t

# Startvärden. Tillför att koden ska kunna köra utan att störas av odefinerade variabler
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
scen2_2_1_1_1_win = ""
scen2_2_1_2_1_win = ""
scen2_2_1_1_1_1_win = ""


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
        t.sleep(2)
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
            return(experience(input("\033[0mHar du spelat spelet förutt? (\033[92mja\033[0m/\033[92mnej\033[0m) \033[93m").lower()))
        
    else:
        print("\033[94mFörsök igen. Skriv (\033[92mja\033[94m/\033[92mnej)\033[94m tack")
        return (experience(input("\033[0mHar du spelat spelet förutt? (\033[92mja\033[0m/\033[92mnej\033[0m) \033[93m").lower()))   


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
        t.sleep(2)

    elif done == "nej":
        print("\033[0mOk. Då kommer rutan igen")
        t.sleep(1.5)
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
    # t.sleep(1)
    print("\033[0mDu är i en fängelse cell")
    t.sleep(2)
    print("Varför?")
    t.sleep(1)
    print("Eftersom du är en tjuv som snor folks donuts")
    t.sleep(3)
    print("Krasch!")
    t.sleep(1.5)
    print("Du krossade ett fönster i cellen som du klättrar ut genom")
    t.sleep(2)
    print("När du landar kommer en polis som heter Wille ur utedasset. Han som fånagde dig förrut!")
    t.sleep(4)
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
    t.sleep(4)


# Funktionen till ditt första val efter man krossat fönstret på sin cell. Kan välja (vänster/framåt/höger).
def scen1(choice):
    t.sleep(1)
    if choice == "vänster":
        print("\033[0mDu träffar på en hund")
        t.sleep(2)
        print("Den är så ful och äcklig att du svimmar av schock!")
        t.sleep(2)
        return False
    
    elif choice == "framåt":
        print("\033[0mDu springer framåt")
        t.sleep(1)
        print("Du hoppar på en en låda och tar sats över stänglset!")
        t.sleep(3)
        print("Precis när du kommer över så fastnar kalsongerna i stängslet (fråga inte hur)")
        t.sleep(5)
        print("Du lyckas inte att komma loss")
        t.sleep(1)
        return False
    
    elif choice == "höger":
        print("\033[0mDu springer iväg")
        t.sleep(2)
        print("På vägen hittar du en pepsi flaska och ett bandage på ett bord som du tar")
        t.sleep(2)
        choice = input("\033[0mSka du distrahera Wille med pepsi flaskan eller dricka den tills senare? (\033[92mdistrahera\033[0m/\033[92mdricka\033[0m) \033[93m").lower()
        if choice == "dricka":
            print("\033[0mDu dricker den")
            t.sleep(1)
            print("Du dricker Willes favorit dricka och han blir rasande och ökar takten")
            t.sleep(4)
            print("Wille kommer i fatt")
            t.sleep(1)
            return False
        
        elif choice == "distrahera":
            print("\033[0mDu slänger flaskan")
            t.sleep(1)
            print("Det var Willes favorit dricka och han blir distraherad av den")
            t.sleep(3)
            print("Du springer vidare och hittar en ficklampa hängandes från en vägg")
            t.sleep(3)
            return True
        
        else:
            print("\033[94mFörsök igen. Skriv (\033[92mdistrahera\033[94m/\033[92mdricka\033[94m) tack!")
            return (scen1(input("\033[0mSka du springa vänster, framåt över stängslet eller höger? (\033[92mvänster\033[0m/\033[92mframåt\033[0m/\033[92mhöger\033[0m) \033[93m").lower()))

    else:
        print("\033[94mFörsök igen. Skriv (\033[92mvänster\033[94m/\033[92mframåt\033[94m/\033[92mhöger\033[94m) tack!")
        return (scen1(input("\033[0mSka du springa vänster, framåt över stängslet eller höger? (\033[92mvänster\033[0m/\033[92mframåt\033[0m/\033[92mhöger\033[0m) \033[93m").lower()))


# Funktionen för den andra scenen, det finns en donut på ett bord. Kan välja (äta/lämna/ta).
def scen2(choice):
    t.sleep(1)
    if choice == "förstöra":
        t.sleep(1)
        print("\033[0mDu springer rakt mot den och slår med all din kraft")
        t.sleep(3)
        print("Av någon anledning")
        t.sleep(1.5)
        print("Slaget var så kraftfullt att armen fastnar i väggen")
        t.sleep(2)
        return False
    
    elif choice == "lämna":
        print("\033[0mDu ignorerar ficklampan och springer vidare")
        t.sleep(3)
        print("Du kommer till en korsning som du springer rakt igenom")
        t.sleep(3)
        print("Efter ett tag hittar du pengar i en väska")
        t.sleep(2.5)
        return choice
    
    elif choice == "ta":
        print("\033[0mDu tog ficklampan")
        t.sleep(1)
        print("Wille kommer nära och kastar sig efter dig!")
        t.sleep(1.5)
        print("Han lyckas inte ta dig men du trillar och skadar dig")
        t.sleep(1.5)
        print("Du är snabbt på fötterna och haltar vidare medans Wille kämpar sig upp")
        t.sleep(3)
        return choice
    
    else:
        print("\033[94mFörsök igen. Skriv (\033[92mäta\033[94m/\033[92mlämna\033[94m/\033[92mta\033[94m) tack!")
        scen2(input("\033[0mSka du förstöra ficklampan, lämna den och dra eller ta den? (\033[92mförstöra\033[0m/\033[92mlämna\033[0m/\033[92mta\033[0m) \033[93m").lower())


# Funktionen för den tredje scenen om man valde att lämna ficklampan i scen2. Kan välja (lämna/ta).
def scen2_1(choice):
    t.sleep(1)
    if choice == "lämna":
        print("\033[0mDu ignorerar pengarna och springer vidare")
        t.sleep(1)
        print("Du hittar ett öppet fönster")
        t.sleep(1)
        return choice
    
    elif choice == "ta":
        print("\033[0mDu sträcker dig efter pengarna")
        t.sleep(1.5)
        print("Precis när du nuddar pengarna kommer knivar rotterandes ut marken")
        t.sleep(3)
        print("Det var en fälla")
        t.sleep(1)
        print("Knivarna skär ditt ben")
        t.sleep(1)
        print("Du inser också att pengarna var fake")
        t.sleep(1)
        print("Du haltar vidare och hittar ett öppet fönster")
        t.sleep(1)
        return choice
        
    else:
        print("\033[94mFörsök igen. Skriv (\033[92mlämna\033[94m/\033[92mta\033[94m) tack!")
        return (scen2_1(input("\033[0mSka du ta pengarna eller springa vidare? (\033[92mlämna\033[0m/\033[92mta\033[0m) \033[93m").lower()))


# Funktionen för den fjärde funktionen om man valde att lämna pengarna i scen2_1. Kan välja (klättra/gå).
def scen2_1_1(choice):
    t.sleep(1)
    if choice == "klättra":
        print("\033[0mDu häver dig upp och klättra genom fönstret")
        t.sleep(2)
        print("Tydligen var byggnaden bara en vägg")
        t.sleep(1.5)
        print("På andra sidan är du utanför fönstret")
        t.sleep(1)
        return True
    
    elif choice == "gå":
        print("\033[0mDu springer vidare")
        t.sleep(1)
        print("Efter ett tag springande kommer du till en återvändsgränd")
        t.sleep(3)
        print("Det fanns inga andra vägar att ta")
        t.sleep(1)
        print("Du vönder dig om och ser Wille kommandes mot dig")
        t.sleep(1)
        return False
    
    else:
        print("\033[94mFörsök igen. Skriv (\033[92mklättra\033[94m/\033[92mgå\033[94m) tack!")
        return (scen2_1_1(input("\033[0mSka du försöka klättra in i fönstret eller gå vidare? (\033[92mklättra\033[0m/\033[92mgå\033[0m) \033[93m").lower()))


# Funktionen för den fjärde funktionen om man valde att ta pengarna i scen2_1. Kan välja (klättra/gå).
def scen2_1_2(choice):
    t.sleep(1)
    if choice == "klättra":
        print("\033[0mDu försöker häva dig upp")
        t.sleep(2)
        print("Men det skadade benet gör det svårt att komma upp")
        t.sleep(3)
        heal = input("\033[0mSka du läka benet med bandaget du fick förut? (\033[92mläka\033[0m/\033[92mklättra\033[0m) \033[93m").lower()
        t.sleep(2)
        if heal == "läka":
            print("\033[0mDu använde bandaget och läkte såret")
            t.sleep(2)
            print("Du försöker igen att klättra och lyckades")
            t.sleep(2)
            print("Byggnaden var en löggn och var bara en vägg")
            t.sleep(1.5)
            print("På andra sidan är friheten")
            t.sleep(1)
            return True

        elif heal == "klättra":
            print("\033[0mDu använde inte bandaget")
            t.sleep(1)
            print("Du försöker klättra men misslyckas")
            t.sleep(1)
            print("Försöker igen men misslyckas")
            t.sleep(1)
            print("Du håller på ett tag tills Wille kommer mot dig")
            t.sleep(2)
            return False

        else:
            print("\033[94mFörsök igen. Skriv (\033[92mläka\033[94m/\033[92mklättra\033[92m) tack!")
            return (scen2_1_2(input("\033[0mSka du försöka klättra in i fönstret eller gå vidare? (\033[92mklättra\033[0m/\033[92mgå\033[0m) \033[93m").lower()))
    
    elif choice == "gå":
        print("\033[0mDu haltar vidare runt alla hörnen")
        t.sleep(1.5)
        print("Men du hammnar istället vid en återvändsgränd")
        t.sleep(2)
        print("Du vänder dig om och Wille står precis bakom dig")
        t.sleep(2)
        return False
    
    else:
        print("\033[94mFörsök igen. Skriv (\033[92mKlättra\033[94m/\033[92mgå\033[94m) tack!")
        return (scen2_1_2(input("\033[0mSka du försöka klättra in i fönstret eller gå vidare? (\033[92mklättra\033[0m/\033[92mgå\033[0m) \033[93m").lower()))


# Funktionen för den tredje scenen om man valde att ta ficklampan i scen2. Kan välja (läka/gå)
def scen2_2(choice):
    t.sleep(1)
    if choice == "läka":
        print("\033[0mDu använde bandaget")
        t.sleep(1)
        print("Bandaget fixade såret och du kan jogga vidare")
        t.sleep(2)
        print("Du joggar vidare och tar vänster i den kommande korsningen")
        t.sleep(3)
        print("Svängen gjorde att Wille tappar bort dig")
        t.sleep(2)
        print("Du ser en port som är lite öppen")
        t.sleep(1)
        return True
    
    elif choice == "gå":
        print("\033[0mDu haltar vidare för att få distans")
        t.sleep(1.5)
        print("Eftersom du är långsamm så kommer Wille i fatt")
        t.sleep(2)
        return False
    
    else: 
        print("\033[94mFörsök igen. Skriv (\033[92mläka\033[94m/\033[92mgå\033[94m) tack")
        return (scen2_2(input("\033[0mSka du läka ditt ben eller gå vidare? (\033[92mläka\033[0m/\033[92mgå\033[0m) \033[93m").lower()))


# Funktionen för den fjärde scenen efter man har läkt sitt ben. kan välja (lämna/ta).
def scen2_2_1(choice):
    t.sleep(1)
    if choice == "in":
        print("\033[0mDu öppnar porten och går in")
        t.sleep(1.5)
        print("Rummet ekar för varje steg")
        t.sleep(1)
        print("Det finns en vatten flaska på ett bord i mitten av rummet")
        t.sleep(2)
        print("Men, det känns skummt")
        t.sleep(1)
        return choice

    elif choice == "vidare":
        print("\033[0mDu går förbi porten utan att titta in")
        t.sleep(2)
        print("Du kommer fram till en korsning")
        t.sleep(1.5)
        return choice
        
    else:
        print("\033[94mFörsök igen. Skriv (\033[92min\033[94m/\033[92mvidare\033[94m) tack!")
        return (scen2_2_1(input("\033[0mSka du gå in genom porten eller vidare? (\033[92min\033[0m/\033[92mvidare\033[0m) \033[93m").lower()))


# Du hittar ett fönster men du är skadad.
def scen2_2_1_1(choice):
    t.sleep(1)
    if choice == "ta":
        print("\033[0mDu går mot flaskan")
        t.sleep(2)
        print("Rummet ekar")
        t.sleep(1)
        print("Du tar den")
        t.sleep(1)
        print("KRASCH!")
        t.sleep(1)
        print("Flaskan var en viktig del av bordet och det rasade")
        t.sleep(2.5)
        print("Det är stor sannolikhet att Wille hörde")
        t.sleep(1.5)
        print("Först måste du bara dricka vattnet då du är törstig och slänga den i plaståtervinningen")
        t.sleep(4)
        print("Det finns en dörr åt vänster och trappor åt höger")
        t.sleep(3)
        return choice
    
    elif choice == "lämna":
        print("\033[0mInstinkterna säger att det är en fälla")
        t.sleep(1.5)
        print("Du lämnar rummet")
        t.sleep(1)
        print("Du springer vidare åt samma håll som innan")
        t.sleep(2)
        return choice
    
    else:
        print("\033[94mFörsök igen. Skriv (\033[92mta\033[94m/\033[92mlämna\033[94m) tack!")
        return (scen2_2_1_1(input("\033[0mSka du ta vatten flaskan eller lämna, ut genom porten? (\033[92mta\033[0m/\033[92mlämna\033[0m) \033[93m").lower()))


# Du hittar ett fönster.
def scen2_2_1_2(choice):
    t.sleep(1)
    if choice == "vänster":
        print("\033[0mDu tar vänster i korsningen")
        t.sleep(1)
        print("Du springer runt alla hörn och förbi alla gränder")
        t.sleep(2)
        print("Efter allt springande kommer du till en återvändsgränd")
        t.sleep(2)
        print("Sedan hör du klampande")
        t.sleep(1.5)
        return False
    
    elif choice == "höger":
        print("\033[0mDu tar höger i korsningen")
        t.sleep(1)
        print("Du springer vidare")
        t.sleep(1)
        print("Du hittar ett öppet fönster över några lådor")
        t.sleep(2)
        return True
    
    else:
        print("\033[94mFörsök igen. Skriv (\033[92mvänster\033[94m/\033[92mhöger\033[94m) tack!")
        return (scen2_2_1_2(input("\033[0mSka du ta vänster eller höger i korsningen? (\033[92mvänster\033[0m/\033[92mhöger\033[0m) \033[93m").lower()))


def scen2_2_1_2_1(choice):
    t.sleep(1)
    if choice == "klättra":
        print("\033[0mDu ställer dig på lådorna och klättra genom fönstret")
        t.sleep(2)
        print("På andra sidan hittar du en nödutgång och går ut ur den")
        t.sleep(2)
        return True
    
    elif choice == "vidare":
        print("033[0mDu springer vidare för att hitta en utgång")
        t.sleep(1.5)
        print("Efter tag kommer du till en återvändsgränd")
        t.sleep(2)
        print("Medan du kollar runt hör du djupa andetag bakom ryggen")
        t.sleep(3)
        return False
    
    else:    
        print("\033[94mFörsök igen. Skriv (\033[92mklättra\033[94m/\033[92mvidare\033[94m) tack!")
        return (scen2_2_1_2_1(input("\033[0mSka du klättra in genom fönstret eller springa vidare? (\033[92mvänster\033[0m/\033[92mhöger\033[0m) \033[93m").lower()))


# vänster genom dörren/höger upp frö trammap
def scen2_2_1_1_1(choice):
    t.sleep(1)
    if choice == "vänster":
        print("\033[0mDu springer vänster mot dörren")
        t.sleep(1)
        print("Du öppnar den och flyger in")
        t.sleep(1)
        print("Inanför fanns det du inte annade")
        t.sleep(2.5)
        print("Du flög rakt in det DÖVAVAKTRUMMET DÄR DÖVAVAKTER VILAR (anledningen till varför de inte hörde bordet)")
        t.sleep(4)
        print("De ser dig och håller dig tills Wille kommer")
        t.sleep(2)
        return False
    
    elif choice == "höger":
        print("\033[0mDu springer höger uppför trappan")
        t.sleep(1.5)
        print("Du springer upp en våning då trappan tog slut")
        t.sleep(2)
        print("Du springer vidare")
        t.sleep(1)
        print("Du ser ett öppet fönster åt höger")
        t.sleep(1)
        return True
    
    else:
        print("\033[94mFörsök igen. Skriv (\033[92mvänster\033[94m/\033[92mhöger\033[94m) tack!")
        return (scen2_2_1_1_1(input("\033[0mSka du ta dörren åt vänster eller trapporna åt höger? (\033[92mvänster\033[0m/\033[92mhöger\033[0m) \033[93m")))



def scen2_2_1_1_1_1(choice):
    t.sleep(1)
    if choice == "höger":
        print("\033[0mDu hoppar ut genom öppna fönstret")
        t.sleep(1.5)
        print("Turen var på din sida")
        t.sleep(1)
        print("Eftersom du landade på en lastbil som åker ut ur fängelset")
        t.sleep(2)
        return True
    
    elif choice == "vidare":
        print("\033[0mDu springer vidare i korridoren")
        t.sleep(1)
        print("Du springer med världens fart")
        t.sleep(1)
        print("Oturen var på din sida")
        t.sleep(1)
        print("Eftersom någon spillt vatten")
        t.sleep(1)
        print("Du halkar och flyger rakt in i vägen och svimmar")
        t.sleep(2)
        return False
    
    else:
        print("\033[94mFörsök igen. Skriv (\033[92mhöger\033[94m/\033[92mvidare\033[94m) tack!")
        return (scen2_2_1_1_1_1(input("\033[0mSka du hopp ut genom fönstret åt höger eller springa vidare? (\033[92mhöger\033[0m/\033[92mvidare\033[0m) \033[93m").lower()))