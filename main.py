import json
import os

def deposit(data, account):
    while True:
        try:
            print("Which account do you want to deposit to?\nPlease select a number for the action you want performed\n1) Checking\n2) Savings")
            choice=int(input("-"))
            if choice==1:
                balance="checkingBalance"
                baltyp="Checking"
            elif choice==2:
                balance="savingsBalance"
                baltyp="Savings"
            elif choice<1 or choice>2:
                print("Invalid number, please try again")
                continue
            amm=float(input("Enter the ammount you would like to deposit (without $ sign) -"))
            data[account]["transactions"].append(f"Deposit into {baltyp} in amount of ${amm:.2f}")
            data[account][balance]+=amm
            with open("accounts.json", "w") as json_file:
                json.dump(data, json_file, indent=4)
        except:
            print("Error")
        print("Invalid number, please try again")


def menu_pick(data, account):
    while True:
        try:
            choice=int(input("-"))
            if choice==1:
                deposit(data, account)
                return False
            elif choice==2:
                withdraw(data, account)#unfinished
                return False
            elif choice==3:
                view_balance(data, account)#unfinished
                return False
            elif choice==4:
                return True
        except:
            print("Error")
        print("invalid choice, please try again")


def get_acc(acc_num, pin, data):
        for i in range(len(data)):
            if data[i]["accountNumber"] == acc_num:
                if data[i]["pin"]==pin:
                    return i
                else:
                    break
        return None


def look_for_data(item, data, data_type, account):
        if data[account][data_type] == item:
                return True
        return False


def load_file():
    try:
        with open ("accounts.json", "r") as file:
            data = json.load(file)
    except Exception:
        print("File Not Found")
        return []
    return data


def sign_in(data):
    while True:
        try:
            acc_num = input("Enter account number: ")
            pin_num = input("Enter PIN number: ")
            account = get_acc(acc_num, pin_num, data)
            if account!=None:
                break
        except:
            print("Error")
        print("invalid account/PIN number, please try again")
    return account


def main():
    data = load_file()
    if data != []:
        account = sign_in(data)
        while True:
            print("""Please select a number for the action you want performed
        1) Deposit
        2) Withdraw
        3) View balance
        4) Exit ATM program
        """)
            exit=menu_pick(data, account)
            if exit==True:
                break
    else:
        print("Accounts File Not Found.")


if __name__=="__main__":
    main()