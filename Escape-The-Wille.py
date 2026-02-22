import FunctionDefinitions as fd


fd.welcome()
while fd.not_played == True:
    played_status = fd.experience(input("\033[0mHar du spelat spelet förutt? (\033[92mja\033[0m/\033[92mnej\033[0m) \033[93m"))
    if played_status == fd.tutorial:
        fd.instructions(fd.tutorial)
        break
    elif played_status == False:
        break

fd.start()
while fd.scen1_win == "":
    scen1_value = fd.scen1(input("\033[0mSka du springa vänster, framåt över stängslet eller höger? (\033[92mvänster\033[0m/\033[92mframåt\033[0m/\033[92mhöger\033[0m) \033[93m").lower())
    if scen1_value == False:
        fd.end("yes")
    elif scen1_value == True:
        fd.scen1_win = True

if fd.scen1_win == True:
    while fd.scen2_win == "":
        scen2_value = fd.scen2(input("\033[0mSka du äta donuten, lämna den och dra eller ta den? (\033[92mäta\033[0m/\033[92mlämna\033[0m/\033[92mta\033[0m) \033[93m").lower())
        if scen2_value == False:
            fd.end("yes")
        elif scen2_value == "lämna":
            fd.scen2_win = "lämna"
        elif scen2_value == "ta":
            fd.scen2_win = "ta"

if fd.scen2_win == "lämna":
    while fd.scen2_1_win == "":
        scen2_1_value = fd.scen2_1(input("\033[0mSka du ta pengarna eller springa vidare? (\033[92mlämna\033[0m/\033[92mta\033[0m) \033[93m").lower())
        if scen2_1_value == False:
            fd.end("yes")
        elif scen2_1_value == "lämna":
            fd.scen2_1_win = "lämna"
        elif scen2_1_value == "ta":
            fd.scen2_1_win = "ta"

if fd.scen2_1_win == "lämna":
    while fd.scen2_1_1_win == "":
        scen2_1_1_value = fd.scen2_1_1(input("\033[0mSka du försöka klättra in i fönstret eller gå vidare? (\033[92mklättra\033[0m/\033[92mgå\033[0m) \033[93m").lower())
        if scen2_1_1_value == False:
            fd.end("yes")
        elif scen2_1_1_value == True:
            fd.end("no")

if fd.scen2_1_win == "ta":
    while fd.scen2_1_2_win == "":
        scen2_1_2_value = fd.scen2_1_2(input("\033[0mSka du försöka klättra in i fönstret eller gå vidare? (\033[92mklättra\033[0m/\033[92mgå\033[0m) \033[93m").lower())
        if scen2_1_2_value == False:
            fd.end("yes")
        elif scen2_1_2_value == True:
            fd.end("no")


if fd.scen2_win == "ta":
    while fd.scen2_2_win == "":
        scen2_2_value = fd.scen2_2(input("\033[0mSka du läka ditt ben eller gå vidare? (\033[92mläka\033[0m/\033[92mgå\033[0m) \033[93m").lower())
        if scen2_2_value == False:
            fd.end("yes")
        elif scen2_2_value == True:
            fd.scen2_2_win = True

    
if fd.scen2_2_win == True:
    while fd.scen2_2_1_win == "":
        scen2_2_1_value = fd.scen2_2_1(input("\033[0mSka du ta pengarna eller gå vidare? (\033[92mta\033[0m/\033[92mlämna\033[0m) \033[93m").lower())
        if scen2_2_1_value == "lämna":
            fd.scen2_2_1_win = "lämna"
        elif scen2_2_1_value == "ta":
            fd.scen2_2_1_win = "ta"


if fd.scen2_2_1_win == "ta":
    while fd.scen2_2_1_1_win == "":
        scen2_2_1_1_value = fd.scen2_2_1_1(input("\033[0mSka du klättra in i fönstret eller gå vidare? (\033[92mklättra\033[0m/\033[92mgå\033[0m) \033[93m").lower())
        if scen2_2_1_1_value == False:
            fd.end("yes")
        elif scen2_2_1_1_value == True:
            fd.end("no")

if fd.scen2_2_1_win == "lämna":
    while fd.scen2_2_1_2_win == "":
        scen2_2_1_2_value = fd.scen2_2_1_2(input("\033[0mSka du klättra in i fönstret eller gå vidare? (\033[92mklättra\033[0m/\033[92mgå\033[0m) \033[93m").lower())
        if scen2_2_1_2_value == False:
            fd.end("yes")
        elif scen2_2_1_2_value == True:
            fd.end("no")