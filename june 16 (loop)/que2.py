# sum of n natural numbers--

sum=0
for i in range(1,11,1):
   sum=sum+i
print("sum of 1 to 10 is: ",sum)

num1 = int(input("Enter Starting value: "))
num2 = int(input("Enter ending value: "))
sum=0
for i in range(num1,num2+1):
   sum=sum+i
print("sum of n natural number is : ",sum)