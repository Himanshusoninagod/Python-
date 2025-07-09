# Bill Calculator--

unit=int(input("Enter unit: "))

if unit>=0 and unit<=50 :
    print("your bill is: ", unit*5)

elif unit>50 and unit<=100 :
    print("your bill is: ", (unit*10)-5)

elif unit>100 and unit<=200 :
    print("your bill is: ", (unit*15)-500-5)

elif unit>200 :
    print("your bill is: ", (unit*20)-500-1500-5)

else :
    print("Invalid Input")