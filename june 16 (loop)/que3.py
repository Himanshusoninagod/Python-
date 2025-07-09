# factorial of a number--
# ex-5
# 1*2*3*4*5=120

fac=1
for i in range(1,5):
    fac=fac*i
print(fac)

num = int(input("Enter Starting value: "))
fac=1
for i in range(1,num+1):
    fac=fac*i
print(fac)


