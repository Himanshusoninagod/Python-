# Find gretest number in a list--
li=[1,2,3,4,15,6,7,8,9,10,20]
ans=li[0]

# pre defined function-- print(max(li))
print(max(li))

# or-

for i in li:
    if (i>ans):
       ans = i
print(ans)

# Find smallest number in a list--
li=[1,2,3,4,15,6,7,8,9,10,20]
ans=li[0]
# pre defined function-- print(min(li))
print(min(li))

# or-

for i in li:
    if (i<ans):
       ans = i
print(ans)