from cmath import inf


d={}
k=-inf
arr=[int(i) for i in input().split()]
# print(arr)
for i in arr:
    # print(i,d)
    if i in d:
        d[i]+=1
        k=max(k,d[i])
        # print(k,k,d[i],d)
    if i not in d:
        d[i]=1
# print(k,d)
if k==-inf:
    k=1
print(len(arr)-k)

# print(d)

#sc o(n) dict python
#tc o(n)
