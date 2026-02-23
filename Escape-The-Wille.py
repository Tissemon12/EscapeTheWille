# Importerar externa filen med definerade funktioner för spelet. Funktionen heter FunctionDefinitions och kallas fd.
import FunctionDefinitions as fd


# Början av spelet
# Börjar med att skriva ut titeln på spelet. Escape The Wille.
fd.welcome()
# Här frågar man om spelaren spelat förut och vissar instruktioner om man inte gjort det.
# While loop för att man ska kunna skriva om om man skrev fel.
while fd.not_played == True:
    # Frågar användaren om de spelat förrut. Om inte, frågas om de vill se instruktioner.
    played_status = fd.experience(input("\033[0mHar du spelat spelet förutt? (\033[92mja\033[0m/\033[92mnej\033[0m) \033[93m"))
    # Om de vill se instruktioner körs denna.
    if played_status == fd.tutorial:
        fd.instructions(fd.tutorial)
        break
    # Om de kört innan eller inte vill se instruktioner körs denna.
    elif played_status == False:
        break

# Vissar intro scenen för spelet är man flyr fängelset.
fd.start()

# ------Generell spelstruktur------
# Först en if sats som kollar om man vunnit tidigare scen (förutom scen1).
# Om man vunnit så körs en while loop med nästa scen (en while loop eftersom om man skrev fel så kan man skriva om).
# I while loopen sparas scenens returnerade värde i scen{n}_value.
# If sats som kollar om man dog eller överlevde.
# False = Man förlorade och skriver förlust text.
# True = Man överlevde och scen{n}_win blir True (har detta system för att kunna hoppa över kod block där scen{n}_win är odefinerade)
# (Måste inte just vara True utan om det finns fler rätta svar så blir scen{n}_win det man svarade)


# Detta är för scenen direkt efter man krossatförnster på sin cell. Kan välja (vänster/framåt/höger).
while fd.scen1_win == "":
    scen1_value = fd.scen1(input("\033[0mSka du springa vänster, framåt över stängslet eller höger? (\033[92mvänster\033[0m/\033[92mframåt\033[0m/\033[92mhöger\033[0m) \033[93m").lower())
    if scen1_value == False:
        fd.end("yes")
    elif scen1_value == True:
        fd.scen1_win = True


# Detta är om man sprang höger i förra scenen. Kan välja (äta/lämna/ta).
if fd.scen1_win == True:
    while fd.scen2_win == "":
        scen2_value = fd.scen2(input("\033[0mSka du äta donuten, lämna den och dra eller ta den? (\033[92mäta\033[0m/\033[92mlämna\033[0m/\033[92mta\033[0m) \033[93m").lower())
        if scen2_value == False:
            fd.end("yes")
        elif scen2_value == "lämna":
            fd.scen2_win = "lämna"
        elif scen2_value == "ta":
            fd.scen2_win = "ta"


# Detta är om man lämnade donuten i förra scenen. Kan välja (lämna/ta).
if fd.scen2_win == "lämna":
    while fd.scen2_1_win == "":
        scen2_1_value = fd.scen2_1(input("\033[0mSka du ta pengarna eller springa vidare? (\033[92mlämna\033[0m/\033[92mta\033[0m) \033[93m").lower())
        if scen2_1_value == False:
            fd.end("yes")
        elif scen2_1_value == "lämna":
            fd.scen2_1_win = "lämna"
        elif scen2_1_value == "ta":
            fd.scen2_1_win = "ta"


# Detta är om man lämnade pengarna i förra scenen. Kan välja (klättra/gå).
if fd.scen2_1_win == "lämna":
    while fd.scen2_1_1_win == "":
        scen2_1_1_value = fd.scen2_1_1(input("\033[0mSka du försöka klättra in i fönstret eller gå vidare? (\033[92mklättra\033[0m/\033[92mgå\033[0m) \033[93m").lower())
        if scen2_1_1_value == False:
            fd.end("yes")
        elif scen2_1_1_value == True:
            fd.end("no")


# Detta är om man tog pengarna i scen2_1. Kan välja (Klättra/gå).
if fd.scen2_1_win == "ta":
    while fd.scen2_1_2_win == "":
        scen2_1_2_value = fd.scen2_1_2(input("\033[0mSka du försöka klättra in i fönstret eller gå vidare? (\033[92mklättra\033[0m/\033[92mgå\033[0m) \033[93m").lower())
        if scen2_1_2_value == False:
            fd.end("yes")
        elif scen2_1_2_value == True:
            fd.end("no")


# Detta är om man tog donuten i scen2. Kan välja (läka/gå).
if fd.scen2_win == "ta":
    while fd.scen2_2_win == "":
        scen2_2_value = fd.scen2_2(input("\033[0mSka du läka ditt ben eller gå vidare? (\033[92mläka\033[0m/\033[92mgå\033[0m) \033[93m").lower())
        if scen2_2_value == False:
            fd.end("yes")
        elif scen2_2_value == True:
            fd.scen2_2_win = True


# Detta är om man klarade förra scenen. Kan välja (lämna/ta). 
if fd.scen2_2_win == True:
    while fd.scen2_2_1_win == "":
        scen2_2_1_value = fd.scen2_2_1(input("\033[0mSka du ta pengarna eller gå vidare? (\033[92mlämna\033[0m/\033[92mta\033[0m) \033[93m").lower())
        if scen2_2_1_value == "lämna":
            fd.scen2_2_1_win = "lämna"
        elif scen2_2_1_value == "ta":
            fd.scen2_2_1_win = "ta"


# Detta är om man tog pengarna i förra scenen. Kan välja (klättra/gå)
if fd.scen2_2_1_win == "ta":
    while fd.scen2_2_1_1_win == "":
        scen2_2_1_1_value = fd.scen2_2_1_1(input("\033[0mSka du klättra in i fönstret eller gå vidare? (\033[92mklättra\033[0m/\033[92mgå\033[0m) \033[93m").lower())
        if scen2_2_1_1_value == False:
            fd.end("yes")
        elif scen2_2_1_1_value == True:
            fd.end("no")


# Detta är om man lämnade pengarna i scen2_2_1. Kan välja (klättra/gå).
if fd.scen2_2_1_win == "lämna":
    while fd.scen2_2_1_2_win == "":
        scen2_2_1_2_value = fd.scen2_2_1_2(input("\033[0mSka du klättra in i fönstret eller gå vidare? (\033[92mklättra\033[0m/\033[92mgå\033[0m) \033[93m").lower())
        if scen2_2_1_2_value == False:
            fd.end("yes")
        elif scen2_2_1_2_value == True:
            fd.end("no")