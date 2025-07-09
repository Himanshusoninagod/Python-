# Nested if--

bank = input("Enter bank/card name: ").lower()
balance=10000

if bank=="sbi" :
    print("Welcome to SBI Banking... ")
    pin = int(input("Enter ATM pin: "))

    if pin==1234 :

        option = int(input("1 for Deposite 2 for withdrawal 3 for Balance Check: "))

        if option==1 :
            amount= int(input("Enter amount you want to deposite: "))
            if amount>0 :
                print("After deposite your updated balance is: ", balance+amount)
            else :
                print("Invalid Input amount")


        elif option==2 :
            amount= int(input("Enter amount you want to withdraw: "))
            if amount>0 and amount<=balance :
                print("After withdrawal your updated balance is: ", balance-amount)
            else :
                print("Invalid Input amount")

        elif option==3 :
            print("Your balance is: ", balance)

        else :
            print("Invalid")
    else :
        print("Incurrect Pin")

else :
    print("Invalid Input")



