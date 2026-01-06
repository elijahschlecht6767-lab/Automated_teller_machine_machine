import json
import os

def look_for_num(asi, data, number_type):
        for i in range(len(data)):
            if data[i][number_type] == asi:
                return True
        return False
    
def load_file():
    try:
        with open ("accounts.json" "r") as file:
            data = json.load(file)
    except Exception:
        print("File Not Found")
        return []
    return data

def sign_in(file):
     while True:
        try:
            acc_num = input("Enter account number: ")
            pin_num = input("Enter PIN number: ")
            acc_check = look_for_num(acc_num, file, "accountNumber")
            pin_check = look_for_num(pin_num, file, "pin")
            if acc_check and pin_check:
                return True
            else:
                print("invalid account/PIN number")
        except:
            print("invalid account/PIN number")

def main():
    file = load_file()
    if file != []:
        account = sign_in(file)
        if account:
            pass
    else:
        print("Accounts File Not Found.")
    #continue here


if __name__=="__main__":
    main()