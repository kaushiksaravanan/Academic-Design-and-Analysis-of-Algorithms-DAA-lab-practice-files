

def z_score(stri,pattern):
    # print(stri)
    k=1
    start=1
    z_array=['x']*len(stri)
    while start<len(stri):
        # print(start)
        c=0
        for i in range(len(stri)-start):
            if stri[i]==stri[i+start]:
                c+=1
            else:
                break
        # print(z_array)
        if c==len(pattern):
            return 'YES'
        z_array[k]=c
        k+=1
        start+=1
    return 'NO'
# print(z_score('aabcaabxaaaz'))
# print(z_score('aaaaaa'))
# print(z_score('aabaacd'))
# print(z_score('abababab'))
print(z_score('bac$baabaa','bac'))



# for _ in range(int(input())):
# 	temp=input().split()
# 	print(lps(temp[0], temp[1]))