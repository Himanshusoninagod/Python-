#1. print first 10 natural numbers using a loop?
# for i in range(1,11):
#     print(i)


#2. write a program to calculate the factorial of a number using a for loop?
# num = int(input("Enter Starting value: "))
# fac=1
# for i in range(1,num+1):
#     fac=fac*i
# print(fac)

#3. sum of first 10 natural numbers?
# sum=0
# for i in range(1,11,1):
#    sum=sum+i
# print("sum of 1 to 10 is: ",sum)

#4. find all numbers divisible by 3 and 5 in a range?
# num1 = int(input("enter starting value: "))
# num2 = int(input("enter ending value: "))
# for i in range(num1,num2+1):
#     if i%3==0 and i%5==0:
#         print(i)

#5. write a program to calculate the sum of squares of the first n natural numbers?
# num1 = int(input("enter starting value: "))
# num2 = int(input("enter ending value: "))
# sum=0
# for i in range(num1,num2+1):
#     sum+=i*i
# print(sum)


#6. print a multiplication table of a given number?
# num=int(input("Enter number: "))
# for i in range(1,11):
#     print(i*num)


#7. prime number (who is divisile by 1 or itself)
# num=int(input("Enter number: "))
# count=0
# for i in  range(1,num+1):
#     if num%i==0 :
#         count=count+1

# if (count==2):
#     print("Prime number")
# else:
#     print("Not a prime number")



#8. implement a program to reverse a number?
# num=int(input("Enter number: "))
# rev=0
# while(num>0):
#     last=num%10
#     rev=rev*10+last
#     num=num//10
# print(rev)


#9. count the number of digit in a number?
# digit=0
# num= int(input("enter a number: "))
# while (num>0) :
#     last=num%10
#     num=num//10
#     digit+=1
# print(digit)


#10.write a program to calculate the sum of digits of a number?
# sum=0
# num= int(input("enter a number: "))
# while (num>0) :
#     last=num%10
#     num=num//10
#     sum=sum+last
# print(sum)


#11. Pallindrom 121==121 123!=321
# num=int(input("Enter number: "))
# ans=num
# rev=0

# while (num>0):
#     last=num%10
#     rev=rev*10+last
#     num=num//10
 
# if (ans==rev):
#     print("Pallindrom Number")
# else:
#     print("Not a Pallindrome Number ")


#12. print all prime number within a given range (who is divisile by 1 or itself)
# num1=int(input("Enter starting number: "))
# num2=int(input("Enter ending number: "))

# for num in  range(num1,num2+1):
#     if num>1:
#         for i in range (2,num):
#             if (num%i==0):
#                 break
#         else:
#             print(num,end=" ")

#13. febonacchi series?
# num=int(input("Enter a number: "))
# a=0
# b=1
# print(a, end=" ")
# print(b, end=" ")
# for i in range(2,num):
#     c=a+b
#     print(c, end=" ")
#     a=b
#     b=c


#14. armstrong number
# num = int(input("Enter number: "))
# sum=0
# ans=num

# while (num>0):
    
#     digit=num%10
#     sum+=digit*digit*digit
#     num/=10
       
# if (ans==sum):
#     print("armstrong number")
    
# else:
#     print("not armstrong number")


#15. sum of all even and odd numbers in a range?
# num= int(input("Enter range: "))
# evsum=0
# odsum=0
# for i in range(num+1):
#     if i%2==0:
#         evsum=evsum+i
#     else:
#         odsum=odsum+i
# print(evsum, end=" ")
# print(odsum, end=" ")

# 16. HCF
# num1 =int(input("Enter num1: "))
# num2 =int(input("Enter num2: "))
# min(num1,num2)
# for i in range(1,min(num1,num2),1):
#     if num1%i==0 and num2%i==0 :
#         hcf=i
# print(hcf)

# 17. LCM
# num1 =int(input("Enter num1: "))
# num2 =int(input("Enter num2: "))
# num3=max(num1,num2)

# while(True):
#     if (num3%num1==0 and num3%num2==0):
#         lcm=num3
#         break
#     num3+=1
# print(lcm)
    


        



 








