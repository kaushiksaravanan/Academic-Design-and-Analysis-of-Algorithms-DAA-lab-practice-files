


letters={'z':2,'k':7,'m':24,'c':32,'u':37,'d':42,'l':42,'e':120}
# letters_sorted=sorted(letters,key=lambda x:letters[x])
r=len(letters)
# [z,0][k,0]
ans={}
while r>=2:
    letters_sorted=list(sorted(letters,key=lambda x:letters[x]))
    # print(letters_sorted)
    if len(letters)==0:
        break
    l1,n1=letters_sorted[0],letters[letters_sorted[0]]
    l2,n2=letters_sorted[1],letters[letters_sorted[1]]
        
    if n1>n2:
        #n2 min

        for letter in l2:
                if letter in ans:
                    ans[letter]='0'+ans[letter]
                if letter not in ans:
                    ans[letter]='0'
        for letter in l1:
            if letter in ans:
                ans[letter]='1'+ans[letter]
            if letter not in ans:
                ans[letter]='1'
        letters[l1+l2]=n1+n2
        
    else:
        for letter in l1:
                if letter in ans:
                    ans[letter]='0'+ans[letter]
                if letter not in ans:
                    ans[letter]='0'
        for letter in l2:
            if letter in ans:
                ans[letter]='1'+ans[letter]
            if letter not in ans:
                ans[letter]='1'

        # if l1 in ans:
        #     ans[l1]='0'+ans[l1]
        # if l1 not in ans:
        #     ans[l1]='0'
        
        # if l2 in ans:
        #     ans[l2]='1'+ans[l2]
        # if l2 not in ans:
        #     ans[l2]='1'
        letters[l1+l2]=n1+n2
        
        
    # print(l1,n1)
    # print(l2,n2)
    del letters[l1]
    del letters[l2]

    r-=1
print(ans)
# for i in ans:
#     if len(i)==1:
#         pass
#     else:
#         y=str(i)
s=input()
a=''
for i in s:
    a+=ans[i]
print(a,len(a))
k=input()
de=''
i=0
while i<len(k):
    # print(i,ddee)
    for l in ans:
        to_con=ans[l]
        # print(to_con)
        if i+len(to_con)<=len(k):
            # print(k[i:i+len(to_con)],k,i,i+len(to_con),de,k[i:])
            if k[i:i+len(to_con)]==ans[l]:
                de+=l
                # print(de)
                i=i+len(to_con)
print(de)
