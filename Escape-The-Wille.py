import FunctionDefinitions as fd


fd.welcome()
if fd.experience(input("Har du spelat spelet förutt? (ja/nej) ")) == fd.tutorial:
    fd.instructions(fd.tutorial)

fd.start()
scen1_value = fd.scen1(input("Ska du springa vänster, framåt över stängslet eller höger? (vänster/framåt/höger) "))
if scen1_value == False:
    fd.end("yes")
elif scen1_value == True:
    scen2_value = fd.scen2(input("Ska du äta donuten, lämna den och dra eller ta den? (äta/lämna/ta) "))
    if scen2_value == False:
        fd.end("yes")
    elif scen2_value == True:
        scen2_1_value = fd.scen2_1(input("Ska du ta pengarna eller springa vidare? (lämna/ta) "))
        if scen2_1_value == False:
            fd.end("yes")
        elif scen2_1_value == True:
            scen2_1_1_value = fd.scen2_1_1(input("Ska du försöka klättra in i fönstret eller gå vidare? (klättra/gå)")).lower()
            if scen2_1_1_value == False:
                fd.end("yes")
            elif scen2_1_1_value == True:
                fd.end("no")
            else:
                print("Skriv rätt dummer")
        else:
            print("Skriv rätt dummer")
    else:
        print("Skriv rätt dummer")
else:
    print("skriv rätt dummer")