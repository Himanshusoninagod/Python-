#Shorting--
# arrange the list in assending order without using function?
# assending--
li=[1,2,6,5,4,7]
for i in range(len(li)):
    for j in range (i+1, len(li)):
        if li[i]>li[j]:
            li[i],li[j]=li[j],li[i]
print(li)

# Arrange the list in desending order without using function?
# desending--
li=[1,2,6,5,4,7]
for i in range(len(li)):
    for j in range (i+1, len(li)):
        if li[i]<li[j]:
            li[i],li[j]=li[j],li[i]
print(li)