# find the frequency of each element present in list?

li=["raj","suraj","raj","ram"]
ans={}
for i in li:
    ans[i]=ans.get(i,0)+1
print(ans)