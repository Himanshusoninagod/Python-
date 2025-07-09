# Shorting--
# find the second largest number in a list?

# short the list in assending order and print li[1]
li=[1,2,6,7,9]
for i in range(len(li)):
    for j in range (i+1,len(li)):
        if li[i]<li[j]:
            li[i],li[j]=li[j],li[i]
print(li)
print(li[1])

# move largest number in a list in starting of the list --
# short the list in assending order and print li[0]
li=[1,2,3,4,5]
k=int(input("Enter value: "))
for i in range(k):
    for j in range (i+1,len(li)):
        if li[i]<li[j]:
            li[i],li[j]=li[j],li[i]
print(li)
print(li[k-1])


# move zero's in the last of the list?

li=[1,0,2,3,0,4]
j=0
for i in range (len(li)):
    if (li[i]!=0):
        li[i],li[j]=li[j],li[i]
        j=j+1
print(li)


# moremoree mejority--

li=[2,3,1,2,2,1,3,1]
for i in range(len(li)-1):
    if (li[i]!=-1):
        freq=1
        for j in range(i+1,len(li)):
            if li[i]==li[j]:
                freq=freq+1
                li[j]=-1
        print("the frequency of:",li[i],"is",freq)





