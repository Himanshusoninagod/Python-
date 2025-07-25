# function - 

# predefine function -
# print()
# len()
# count()
# index()
# sort()

# User define function -
# reusability of code 
# Readnility of code 

# def - keyword (define) 
# return-                       # NonReturn-
# with arguement                # with arguement    
# without arguement             # without arguement


#1. non return without argument
# def multi():
#     a=int(input("Enter first Number: "))
#     b=int(input("Enter Second Number: "))
#     print(a*b)

# multi()

 

#2. non return with argument
# def multi(a,b):
#     print(a*b)

# x=int(input("Enter first Number: "))
# y=int(input("Enter Second Number: "))
# multi(x,y) 



#3. return typr without arguement 
# def multi():
#     a=int(input("enter a number:"))
#     b=int(input("enter a number:"))
#     return a*b 
# ans=multi()
# print(ans)



#4. return type with arguement 
# def multi(a,b):
#     return a*b
# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# ans=multi(a,b)
# print(ans)

# def is_prime(num):
#     for i in range(2,num):
#         if(num%i==0):
#             return "Not a prime"
#     return "prime"
# print(is_prime())



# factorial -- 
def fectorial(n):
    fac=1
    for i in range(1,n+1):
        fac*=i
    return fac

n=int(input("Enter a number:"))
print(fectorial(n))
        














