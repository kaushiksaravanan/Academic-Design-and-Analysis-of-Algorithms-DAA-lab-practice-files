
arr=[int(i) for i in input().split()]
d={}
max_len=-99999
for i in range(len(arr)):
    if arr[i] in  d:
        min_ind=d[arr[i]]
        max_ind=i
        max_len=max(max_len,max_ind-min_ind)
    if arr[i] not in d:
        d[arr[i]]=i
print(max_len)

#tc o(n)
#sc o(n) dict