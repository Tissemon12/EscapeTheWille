# Importerar externa filen med definerade funktioner för spelet. Funktionen heter FunctionDefinitions och kallas fd.
import FunctionDefinitions as fd


# Början av spelet
# Börjar med att skriva ut titeln på spelet. Escape The Wille.
fd.welcome()

# Funktionen frågar användaren om de spelat förrut och om de vill se instruktionerna
if fd.experience(input("\033[0mHar du spelat spelet förutt? (\033[92mja\033[0m/\033[92mnej\033[0m) \033[93m").lower()) == "ja":
    fd.instructions("ja")

# Vissar intro scenen för spelet när man flyr fängelset och frågar om man vill se den (tar lång tid).
fd.start(input("\033[0mVill du se intro scenen? (\033[92mja\033[0m/\033[92mnej\033[0m) \033[93m"))

# ------Generell spelstruktur------
# Först en if sats som kollar om man vunnit tidigare scen (förutom scen1).
# I if satsen sparas scenens returnerade värde i scen{n}_value från motsvarande funktion.
# If sats som kollar om man dog eller överlevde.
# False = Man förlorade och skriver förlust text.
# True = Man överlevde och scen{n}_win blir True (Används för att kunna hoppa över kod block som inte ska köras. Man gjorde ett annat val)
# (Måste inte just vara True utan om det finns fler rätta svar så blir scen{n}_win det man svarade)


# --- Scen 1 ---
# Detta är scenen direkt efter man krossatförnster på sin cell. Kan välja (vänster/framåt/höger).
scen1_value = fd.scen1(input("\033[0mSka du springa vänster, framåt över stängslet eller höger? (\033[92mvänster\033[0m/\033[92mframåt\033[0m/\033[92mhöger\033[0m) \033[93m").lower())
if scen1_value == False:
    fd.end("yes")
elif scen1_value == True:
    fd.scen1_win = True


# --- Scen 2 ---
# Detta är om man sprang höger i scen 1. Kan välja (äta/lämna/ta).
if fd.scen1_win == True:
    scen2_value = fd.scen2(input("\033[0mSka du förstöra ficklampan, lämna den och dra eller ta den? (\033[92mförstöra\033[0m/\033[92mlämna\033[0m/\033[92mta\033[0m) \033[93m").lower())
    if scen2_value == False:
        fd.end("yes")
    elif scen2_value == "lämna":
        fd.scen2_win = "lämna"
    elif scen2_value == "ta":
        fd.scen2_win = "ta"


# --- Scen 2_1 ---
# Detta är om man lämnade ficklampan i scen 2_1. Kan välja (lämna/ta).
if fd.scen2_win == "lämna":
    scen2_1_value = fd.scen2_1(input("\033[0mSka du ta pengarna eller springa vidare? (\033[92mlämna\033[0m/\033[92mta\033[0m) \033[93m").lower())
    if scen2_1_value == False:
        fd.end("yes")
    elif scen2_1_value == "lämna":
        fd.scen2_1_win = "lämna"
    elif scen2_1_value == "ta":
        fd.scen2_1_win = "ta"


# --- Scen 2_1_1 ---
# Detta är om man lämnade pengarna i scen 2_1. Kan välja (klättra/gå).
if fd.scen2_1_win == "lämna":
    scen2_1_1_value = fd.scen2_1_1(input("\033[0mSka du försöka klättra in i fönstret eller gå vidare? (\033[92mklättra\033[0m/\033[92mgå\033[0m) \033[93m").lower())
    if scen2_1_1_value == False:
        fd.end("yes")
    elif scen2_1_1_value == True:
        fd.end("no")


# --- Scen 2_1_2 ---
# Detta är om man tog pengarna i scen 2_1. Kan välja (Klättra/gå).
if fd.scen2_1_win == "ta":
    scen2_1_2_value = fd.scen2_1_2(input("\033[0mSka du försöka klättra in i fönstret eller gå vidare? (\033[92mklättra\033[0m/\033[92mgå\033[0m) \033[93m").lower())
    if scen2_1_2_value == False:
        fd.end("yes")
    elif scen2_1_2_value == True:
        fd.end("no")


# --- Scen 2_2 ---
# Detta är om man tog ficklampan i scen 2. Kan välja (läka/gå).
if fd.scen2_win == "ta":
    scen2_2_value = fd.scen2_2(input("\033[0mSka du läka ditt ben eller gå vidare? (\033[92mläka\033[0m/\033[92mgå\033[0m) \033[93m").lower())
    if scen2_2_value == False:
        fd.end("yes")
    elif scen2_2_value == True:
        fd.scen2_2_win = True


# --- Scen 2_2_1 ---
# Detta är om man klarade scen 2_2. Kan välja (lämna/ta). 
if fd.scen2_2_win == True:
    scen2_2_1_value = fd.scen2_2_1(input("\033[0mSka du gå in genom porten eller vidare? (\033[92min\033[0m/\033[92mvidare\033[0m) \033[93m").lower())
    if scen2_2_1_value == "in":
        fd.scen2_2_1_win = "in"
    elif scen2_2_1_value == "vidare":
        fd.scen2_2_1_win = "vidare"


# --- Scen 2_2_1_1 ---
# Detta är om man gick in i porten i scen 2_2_1. Kan välja (klättra/gå).
if fd.scen2_2_1_win == "in":
    scen2_2_1_1_value = fd.scen2_2_1_1(input("\033[0mSka du ta vatten flaskan eller lämna, ut genom porten? (\033[92mta\033[0m/\033[92mlämna\033[0m) \033[93m").lower())
    if scen2_2_1_1_value == "ta":
        fd.scen2_2_1_1_win = "ta"
    elif scen2_2_1_1_value == "lämna":
        fd.scen2_2_1_1_win = "lämna"


# --- Scen 2_2_1_2 ---
# Detta är om man inte gick in i porten i scen 2_2_1. Kan välja (klättra/gå).
if fd.scen2_2_1_win == "vidare":
    scen2_2_1_2_value = fd.scen2_2_1_2(input("\033[0mSka du ta vänster eller höger i korsningen? (\033[92mvänster\033[0m/\033[92mhöger\033[0m) \033[93m").lower())
    if scen2_2_1_2_value == False:
        fd.end("yes")
    elif scen2_2_1_2_value == True:
        fd.scen2_2_1_2_win = True


# --- Scen 2_2_1_1_1 ---
# Detta är om man vattenflaskan på bordet i scen 2_2_1_1. Kan välja (vänster/höger).
if fd.scen2_2_1_1_win == "ta":
    scen2_2_1_1_1_value = fd.scen2_2_1_1_1(input("\033[0mSka du ta dörren åt vänster eller trapporna åt höger? (\033[92mvänster\033[0m/\033[92mhöger\033[0m) \033[93m"))
    if scen2_2_1_1_1_value == False:
        fd.end("yes")
    elif scen2_2_1_1_1_value == True:
        fd.scen2_2_1_1_1_win = True


# --- Scen 2_2_1_2 ---
# Detta är om man lämnade vattenflaskan och gick tillbacka samma väg i scen 2_2_1_1. Kan välja (vänster/höger).
if fd.scen2_2_1_1_win == "lämna":
    scen2_2_1_2_value = fd.scen2_2_1_2(input("\033[0mSka du ta vänster eller höger i korsningen? (\033[92mvänster\033[0m/\033[92mhöger\033[0m) \033[93m").lower())
    if scen2_2_1_2_value == False:
        fd.end("yes")
    elif scen2_2_1_2_value == True:
        fd.scen2_2_1_2_win = True


# --- Scen 2_2_1_2_1 ---
# Detta är om man tog höger i korsnigen i scen 2_2_1_2. Kan välja (klättra/vidare).
if fd.scen2_2_1_2_win == True:
    scen2_2_1_2_1_value = fd.scen2_2_1_2_1(input("\033[0mSka du klättra in genom fönstret eller springa vidare? (\033[92mklättra\033[0m/\033[92mvidare\033[0m) \033[93m").lower())
    if scen2_2_1_2_1_value == False:
        fd.end("yes")
    elif scen2_2_1_2_1_value == True:
        fd.end("no")


# --- Scen 2_2_1_1_1_1 ---
# Detta är om man sprang höger uppför trapprona i scen 2_2_1_1_1. Kan välja (höger/vidare).
if fd.scen2_2_1_1_1_win == True:
    scen2_2_1_1_1_1_value = fd.scen2_2_1_1_1_1(input("\033[0mSka du hoppa ut genom fönstret åt höger eller springa vidare? (\033[92mhöger\033[0m/\033[92mvidare\033[0m) \033[93m").lower())
    if scen2_2_1_1_1_1_value == False:
        fd.end("yes")
    elif scen2_2_1_1_1_1_value == True:
        fd.end("no")