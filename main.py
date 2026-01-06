import json
import os

def lookfornum(asi):
    with open("accounts.json", "r") as jsonfile:
        data = json.load(jsonfile)
        for i in range(len(data)):
            if int(data[i]["accountNumber"])==asi:
                return i
        print(len(data))
        return None


def main():
    brreak=0
    notfound=0
    if os.path.exists("accounts.json"):
        notfound=0
    else:
        print("accounts file not found")
        notfound=1
    if notfound==0:
        while True:
            if brreak==1:
                break
            try:
                asi=int(input("Enter account number: -"))
                datanum=lookfornum(asi)
                print(datanum)
                if datanum!=None:
                    while True:
                        try:
                            pin=int(input("Enter pin number: -"))
                            with open("accounts.json", "r") as jsonfile:
                                data = json.load(jsonfile)
                            if int(data[datanum]["pin"])==pin:
                                brreak=1
                                break
                            else:
                                print("invalid pin number")
                        except:
                            print("invalid pin number")
                else:
                    print("invalid account number")
            except:
                print("invalid account number")
    if notfound==0:
        print("""Please select a number for the action you want performed
    1) Deposit
    2) Withdraw
    3) View balance
    4) Exit ATM program
    """)
        #continue here


if __name__=="__main__":
    main()