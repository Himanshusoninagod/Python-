# target sum?
# li=[1,2,4,6,3]
# target=10

li=[1,2,4,6,3]
target=10
for i in range(len(li)):
    for j in range(i+1, len(li)):
        
        if (li[i]+li[j]==10):
            print(li[i],li[j])