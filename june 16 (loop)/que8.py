# perfect number - 6(divisible bye 1,2,3 and sum of these are also 6),28,496,8128

num= int(input("Enter a number: "))
sum=0

for i in range(1,num):
    if (num%i==0):
        sum=sum+i

if (sum==num):
    print("Perfect Number")

else :
    print("Not a perfect number")