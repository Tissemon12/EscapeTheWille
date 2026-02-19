import FunctionDefinitions as fd


fd.welcome()
if fd.experience(input("Har du spelat spelet förutt? (ja/nej) ")) == fd.tutorial:
    fd.instructions(fd.tutorial)

fd.start()
scen1_value = fd.scen1(input("Ska du springa vänster, framåt över stängslet eller höger? (vänster/framåt/höger) "))
if scen1_value == False:
    fd.end("yes")
elif scen1_value == True:
    scen2_value = fd.scen2(input("Ska du förstöra donuten, lämna den och dra eller ta den? (förstöra/lämna/ta) "))
    if scen2_value == False:
        fd.end("yes")
    elif scen2_value == True:
        scen3_value = fd.scen3(input("Ska du ta pengarna eller springa vidare? (lämna/ta) "))
        if scen3_value == False:
            fd.end("yes")
        elif scen3_value == True:
            pass
        else:
            print("Skriv rätt dummer")
    else:
        print("Skriv rätt dummer")
else:
    print("skriv rätt dummer")