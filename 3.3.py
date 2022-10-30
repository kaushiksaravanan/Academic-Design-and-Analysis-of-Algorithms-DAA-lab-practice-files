# 4, 1, 1, 2, 2, 1, 3, 3
arr=[int(i) for i in input().split()]
# x=int(input())
# prefix frequency
d={}
for i in arr:
    if i in d:
        d[i]+=1
    if i not in d:
        d[i]=1

# print(d)
fin=[]
x=(sorted(d,key=lambda l:d[l]))[::-1]
def find_min(x,m):
    global fin
    pre=[0]*len(arr)
    # print(x)
    if arr[0]==x:
        pre[0]=1
    for i in range(1,len(arr)):
        if arr[i]==x:
            pre[i]=pre[i-1]+1
        else:
            pre[i]=pre[i-1]

    start=0
    end=0
    l=0
    for i in pre:
        # print(i)
        if i==1:
            start=l
        if i==d[x]:
            end=l
            break

        l+=1
    # print(*arr[start:end+1])
    m=min(m,end+1-start)
    if m==end+1-start:
        fin=arr[start:end+1]


same_freq=set()
# same_freq.add
high_freq=x[0]
for i in x:
    if d[high_freq]==d[i]:
        same_freq.add(i)
# print(same_freq)
for i in same_freq:
    find_min(i,99999)
print(*fin)

#sc o(1)
#tc o(1)