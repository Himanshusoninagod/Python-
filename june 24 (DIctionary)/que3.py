# find the student with highest marks?
# data={
#     "jatin":55,
#     "raj":90,
#     "rahul":80
# } output-raj

data={
    "jatin":55,
    "raj":90,
    "rahul":80
}
# print(max(data))

mx=0
for i,j in data:
    if data[i]>mx:
        mx=data[i]
        ans=i
print(ans)

