# calculator--

num1=int(input("Enter num1 value: "))
num2=int(input("Enter num2 value: "))
operation = input("+ - * / % // ** ")

if operation=="+":
     print(num1+num2)

elif operation=="-" :
     print(num1-num2)

elif operation=="*" :
     print(num1*num2)

elif operation=="/" :
     print(num1/num2)

elif operation=="%" :
     print(num1%num2)

elif operation=="//" :
     print(num1//num2)

elif operation=="**" :
     print(num1**num2)

else:
     print("Invalid Input")

