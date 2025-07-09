# Pallindrom 121==121 123!=321

num=int(input("Enter number: "))
ans=num
rev=0

while (num>0):
    last=num%10
    rev=rev*10+last
    num=num//10
 
if (ans==rev):
    print("Pallindrom Number")
else:
    print("Not a Pallindrome Number ")