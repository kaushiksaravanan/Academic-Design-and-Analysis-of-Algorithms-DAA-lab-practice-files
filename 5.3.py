x=[int(i) for i in input().split()]
m=x[0]
n=x[1]
Graph=[[i] for i in range(m)]
visited=[False for i in range(m)]

for i in range(n):
    temp=[int(i) for i in input().split()]
    # print(temp)
    Graph[temp[0]-1].append(temp[1]-1)
    # Graph[temp[0]-1].append(temp[0]-1)
c=0
l=0
count=[]
if True:
    start=0
    stack=[start]
    visited[start]=True
    while len(stack)!=0:
        val=stack.pop()
        visited[val]=True
        count.append(val)
        for i in Graph[val][1:]:
            if visited[i]==False:
                if stack.count(i)==0:
                    stack.append(i)
    if count==m:
        c+=1
    l+=1
if 1 in count:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
