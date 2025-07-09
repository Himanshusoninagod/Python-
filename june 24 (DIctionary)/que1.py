# find the frequency of each element present in list?

s="hellowordpython"
ans={}
for i in s:
    if i in ans:
        ans[i]=ans.get(i)+1
    else:
        ans[i]=1
print(ans)

# or 

s="hello"
ans={}
for i in s:
    ans[i]=ans.get(i,0)+1
print(ans)

