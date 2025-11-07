# decorater in python -

# def add(num):
#     z = even(num)
#     return z

# def even(num):
#     even = [i*2 for i in range(1,num+1)]
#     return even

# num=int(input("Enter number: "))
# add(num)


# comprehention - list,dictinary,set 
# x = [i for i in range(10)]
# print(x)

# x = [i for i in range(10) if i%2==0]
# print(x)


# y = tuple(i for i in range(10))
# print(y)

x = [(x,y) for x in range(2) for y in range(3)]
print(x)