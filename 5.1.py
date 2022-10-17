arr=[]
t=[int(i) for i in input().split()]
n=t[0]
que=t[1]
ind={}
graph=[[i] for i in range(n)]
for _ in range(que):
    x=[int(i) for i in input().split()]
    graph[x[0]-1].append(x[1]-1)
    if x[1]-1 in ind:
        ind[x[1]-1]+=1
    if x[1]-1 not in ind:
        ind[x[1]-1]=1
for i in range(1,n+1):
    if i not in ind:
        ind[i]=0
    # if i not in oud:
    #   oud[i]=0

def check(arr):
    l=0
    c=0
    for i in arr:
        if arr[i]<0:
            c+=1
        l+=1
    return c!=l
order=[]
while check(ind):
    c=0
    l=0
    for i in range(1,n+1)[::-1]:
        if ind[i]==0:
            order.append(i)
            ind[i]-=1
            l+=1	
        c+=1
    if c==l:
        break
    if l==0:
        for i in range(1,n+1):
            if ind[i]>0:
                # print(graph[i-1])
                for x in graph[i-1][1:]:
                    ind[x]-=1
                    # order.append(x)
if len(order)!=n:
    print('NOT POSSIBLE')
else:
    print(order[::-1])
