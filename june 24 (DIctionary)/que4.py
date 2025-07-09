# anagram or not anagram? 

s1="anagram"
s2="aaagrnz"

if len(s1) != len(s2):
    print("Not an angarm")

else:
    freq={}
    for i in s1:
        freq[i]=freq.get(i,0)+1

    for j in s2:
        if j in freq:
            freq[j]-=1

    ans=True
    for i in freq.values():
        if i!=0:
            ans=False
    
    if(ans):
        print("Anagram")
    else:
        print("Not an anagram")

        

