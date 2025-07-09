# ATM --- (Balance=1000)
# 1. Withdrawl
# 2. Deposite
# 3. balance Check
# .lower()

print("1 for Withdrawal 2 for Deposite 3 for Balance Check")
option=int(input("Enter Option: "))
balance=10000

if option==1 :
    amount=int(input("Enter Amount: "))
    print("After withdrawl your remaining amount is: ", balance-amount)

elif option==2:
    amount=int(input("Enter Amount: "))
    print("After deposite your updated amount is: ", balance+amount)

elif option==3 :
    print("Your Balance is: ", balance)

else :
    print("Invalid Input")