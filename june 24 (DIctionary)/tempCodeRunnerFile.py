s="hello"
ans={}
for i in s:
    ans[i]=ans.get(i,0)+1
print(ans)