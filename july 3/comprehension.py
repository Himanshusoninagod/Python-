# if i=='a' or i=='e' or i=='i' or i=='o' or i=='u'
# list,tuple,set,dictionary comprehension--

# li = [ output for i in range() if ]

# print (1-10)
# li = [i for i in range(1,11)]
# print(li)

# table--
# li = [4*i for i in range(1,11)]
# print(li)

# even number--
# li = [i for i in range(1,11) if i%2==0]
# print(li)

# Odd number--
# li = [i for i in range(1,11) if i%2!=0]
# print(li)

# li=list()
# for i in range(1,11):
#     li.append(i)
# print(li)

# create a list of word which have more then 4 charecter?
# input=["aman","raj","rahul","jatin","pratima","gauri","prince"]

# li = ["aman","raj","rahul","jatin","pratima","gauri","prince"]
# li =[i for i in li if len(i)>=4]
# print(li)


# use a list comprehension to filter out onli neg. numbers?
# input = [12,-7,5,64,-14]
# output = [-7,-14]

# li = [12,-7,5,64,-14]
# li = [i for i in li if i<0]
# print(li)

 
# use list comprehension to extract all vowels?
# input = ["hello","world"]
# output =['e','o','o']

# li = "hello world"
# li = [i for i in li if  i in "aeiou" ]
# print(li)


# create a list where keys are numbers from 1 to 5 and value are square?
# output-[{1: 1}, {2: 4}, {3: 9}, {4: 16}, {5: 25}]
# li= [{i:i*i} for i in range(1,6)]
# print(li)


# input="education"
# output=['e', 'u', 'a', 'i', 'o']
# li = "education"
# li = { i for i in li if i in "aeiou"}
# print(li)

# data = {'item1':120,'item2':130,'item3':30}
# ans = { key:value for key,value in data.items() if value>100}
# print(ans)

# li =["data","scirnce","python"]
# ans = {i:len(i) for i in li}
# print(ans)

# [ecpression for i in expression if <expression>]

# li = [i if i%2==0 else i for i in range(1,11) if i>5]
# print(li)

# prime numbers using list comprehension 
# ans = [i for i in range(1,101) if all(i%j!=0 for j in range(2,int(i**0.5)+1))]
# print(ans)

# for i in range(1,101):
#     is_prime=True
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             is_prime=False
#     if is_prime:
#         print(i)

# touple comprehensipon--
# tu = (i*i for i in range(1,11))
# tu = list(tu)
# print(tu)

# for i in tu:
#     print(i,end=" ")

li = [1,2,3,4]
ans = [True if [i for i in li if li.count(i)>1 ] else False ]
print(ans)




