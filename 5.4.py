x=[int(i) for i in input().split()]
m=x[0]
n=x[1]
Graph=[[i] for i in range(m)]
visited=[False for i in range(m)]

for i in range(n):
    temp=[int(i) for i in input().split()]
    # print(temp)
    Graph[temp[0]-1].append(temp[1]-1)
c=0
l=0
for start in range(m):
    count=0
    stack=[start]
    visited[start]=True
    while len(stack)!=0:
        val=stack.pop()
        visited[val]=True
        count+=1
        for i in Graph[val][1:]:
            if visited[i]==False:
                if stack.count(i)==0:
                    stack.append(i)
    if count==m:
        c+=1
    l+=1
if c==l:
    print('YES')
else:
    print('NO')
