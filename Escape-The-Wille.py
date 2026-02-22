import FunctionDefinitions as fd


fd.welcome()
if fd.experience(input("Har du spelat spelet förutt? (ja/nej) ")) == fd.tutorial:
    fd.instructions(fd.tutorial)

fd.start()
scen1_value = fd.scen1(input("Ska du springa vänster, framåt över stängslet eller höger? (vänster/framåt/höger) ").lower())
if scen1_value == False:
    fd.end("yes")
    exit()
elif scen1_value == True:
    scen1_win = True
else:
    print("skriv rätt dummer")

if scen1_win == True:
    scen2_value = fd.scen2(input("Ska du äta donuten, lämna den och dra eller ta den? (äta/lämna/ta) ").lower())
    if scen2_value == False:
        fd.end("yes")
        exit()
    elif scen2_value == "lämna":
        scen2_win = "lämna"
    elif scen2_value == "ta":
        scen2_win = "ta"
    else:
        print("Skriv rätt dummer")

if scen2_win == "lämna":
    scen2_1_value = fd.scen2_1(input("Ska du ta pengarna eller springa vidare? (lämna/ta) ").lower())
    if scen2_1_value == False:
        fd.end("yes")
        exit()
    elif scen2_1_value == True:
        scen2_1_win = True
    else:
        print("Skriv rätt dummer")

if scen2_1_win == True:
    scen2_1_1_value = fd.scen2_1_1(input("Ska du försöka klättra in i fönstret eller gå vidare? (klättra/gå)").lower())
    if scen2_1_1_value == False:
        fd.end("yes")
        exit()
    elif scen2_1_1_value == True:
        fd.end("no")
        exit()
    else:
        print("Skriv rätt dummer")

if scen2_win == "ta":
    scen2_2_value = fd.scen2_2(input("Ska du läka ditt ben eller gå vidare? (läka/gå) ").lower())
    if scen2_2_value == False:
        fd.end("yes")
        exit()
    elif scen2_2_value == True:
        scen2_2_win = True
    else:
        print("Skriv rätt dummer")
    
if scen2_2_win == True:
    scen2_2_1_value = fd.scen2_2_1(input("Ska du ta pengarna eller gå vidare? (ta/lämna) ").lower())
    if scen2_2_1_value == "lämna":
        scen2_2_1_win = "lämna"
    elif scen2_2_1_value == "ta":
        scen2_2_1_win = "ta"
    else:
        print("Skriv rätt dummer")

if scen2_2_1_win == "ta":
    scen2_2_1_1_value = fd.scen2_2_1_1(input("Ska du klättra in i fönstret eller gå vidare? (klättra/gå) ").lower())
    if scen2_2_1_1_value == False:
        fd.end("yes")
        exit()
    elif scen2_2_1_1_value == True:
        fd.end("no")
        exit()

if scen2_2_1_win == "lämna":
    scen2_2_1_2_value = fd.scen2_2_1_2(input("Ska du klättra in i fönstret eller gå vidare? (klättra/gå) ").lower())
    if scen2_2_1_2_value == False:
        fd.end("yes")
        exit()
    elif scen2_2_1_2_value == True:
        fd.end("no")
        exit()