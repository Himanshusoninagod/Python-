# Purchase amount ---
# 0-500 (5% discount)
# 500-2000 (10% discount)
# 2000-10000 (15% discount)
# above 10000 (20% discount)

amount=int(input("Enter Amount: "))
if amount>=0 and amount <=500 :
    print("After discount your bill amount is: ", amount-(amount*5/100))

elif amount>500 and amount <=2000 :
    print("After discount your bill amount is: ", amount-(amount*10/100))

elif amount>2000 and amount <=10000 :
    print("After discount your bill amount is: ", amount-(amount*15/100))

elif amount>10000 :
    print("After discount your bill amount is: ", amount-(amount*20/100))

else :
    print("Invalid Input")