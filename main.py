import json

def lookfornum(asi):
    with open("accounts.json", "r") as jsonfile:
        data = json.load(jsonfile)
        for i in range(len(data)):
            if data[i]["accountNumber"]==asi:
                return i
        return None


def main():
    notfound=0
    try:
        with open ("accounts.json" "r") as diddy:
            data0=json.load(diddy)
    except:
        print("accounts file not found")
        notfound=1
    if notfound==0:
        while True:
            try:
                asi=int(input("Enter account number: -"))
                datanum=lookfornum(asi)
                if datanum!=None:
                    while True:
                        try:
                            pin=int(input("Enter pin number: -"))
                            with open("accounts.json", "r") as jsonfile:
                                data = json.load(jsonfile)
                            if data[datanum]["pin"]==pin:
                                break
                            else:
                                print("invalid pin number")
                        except:
                            print("invalid pin number")
                else:
                    print("invalid account number")
            except:
                print("invalid account number")
        #continue here


if __name__=="__main__":
    main()