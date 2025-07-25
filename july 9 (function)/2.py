# Positional Arguement-
# def add(x,y):
#     z=x+y
#     return z
# p = int(input("enter first value: "))
# q = int(input("enter second value: "))
# print(add(p,q,10))


# Default arguement-

# def add(x=0,y=0):
#     z=x+y
#     return z
# p = int(input("enter first value: "))
# q = int(input("enter second value: "))
# print(add())

# def add(x=0,y=0):
#     z=x+y
#     return z
# p = int(input("enter first value: "))
# q = int(input("enter second value: "))
# print(add(p))

# def add(x=0,y=0):
#     z=x+y
#     return z
# p = int(input("enter first value: "))
# q = int(input("enter second value: "))
# print(add(p,q))

# def add(x=0,y=0):
#     z=x+y
#     return z
# p = int(input("enter first value: "))
# q = int(input("enter second value: "))
# print(add(p,q,10))



# Variable Length Arguement-

# def add(*args):
#     print(args)
#     print(type(args))

# add(2,4)
# add(2,4,6,8,10,20)
# add(2,1,2,3,4,5,6,10,20,440)


# Variable length Arguement-
# for tuple we use single *
# def add(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     return sum
# print(add())
# print(add(1,2,3,4,5))

# x = eval(input("enter any value: "))
# print(type(x))

# x=eval('4+5-2')
# print(x)

# z=3x+4y

# x=10
# y=20
# z= eval('3*x+4*y')
# print(z)

#4. Key-word Arguement-
# def new (x,y,z):
#     print(x,y,z)
#     return x+y+z
# print(new(x=3,y=4,z=5))


#5. Variable length kay-word arguement-
# for dictunary we use double **
# def mydict(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# mydict(x=10,y=20,z=30,p=40,q=50)
# print(mydict)


# mydict={
#     'x':10,
#     'y':20,
#     'z':30,
#     'p':40,
#     'q':50
# }
# sum=0
# for i in mydict.values():
#     sum=sum+i
# print(sum)

# def mydict(**kwargs):
#     sum=0
#     for i in kwargs.values():
#         sum+=i
#     return sum
# print(mydict(
#     x=10,
#     y=20,
#     z=30,
#     p=40,
#     q=50))

def isprime(x):
    
    










