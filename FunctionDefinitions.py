import time as t

def welcome():
    played = input("Spelat förrut (ja/nej)? ")
    if played == "ja":
        print("ok")
        t.sleep(1)
        print("Då startar det")
        return
    elif played == "nej":
        want = input("Vill du se hur man spelar spelet (ja/nej)?")
        if want == "nej":
            print("ok")
            t.sleep(1)
            
