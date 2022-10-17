e=int(input())
graph=[[0 for i in range(e+1)] for i in range(e)]
for i in graph:
    print(*i)


x=[]
for _ in range(int(input())):
    t=[int(i) for i in input().split()]
    graph[t[0]][t[1]]=t[2]
    x.append((min(t[0],t[1]),max(t[0],t[1]),t[2]))
    graph[t[1]][t[0]]=t[2]
print(x)

'''
7
8
0 1 2
0 3 3
0 6 4
1 2 3
1 4 2
3 4 5
6 4 6
4 5 7


'''


visited=[0]
start_index=[0]
done={}
l=0
while len(visited)+1<=e:
    print(done)
    t=[]
    for i in x:
        if i[0] in start_index and i not in done:
                t.append(i)
    # t.sort(key=lambda x:x[2],reverse=True)
    t=sorted(t,key=lambda y:y[2])
    print(t,visited,start_index,l)
    for i in t[::-1]:
        if i[1] in visited:
            pass
        if i[1] not in visited:
            xx=i
    # xx=t[0]
    # if xx[1] in visited:
        # continue
    start_index.append(xx[1])
    visited.append(xx[1])
    done[xx]=1
    l+=xx[2]
print(visited)
print(start_index)
print(l,done)

'''
9
15
0 1 4
0 7 8
1 7 11
1 2 8
7 8 7
7 6 1
6 5 2
6 8 6
2 8 2
2 5 4
2 3 7
2 5 4
3 5 14
3 4 9
5 4 10
'''