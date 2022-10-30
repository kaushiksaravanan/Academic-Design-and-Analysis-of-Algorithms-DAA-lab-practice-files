x=[int(i) for i in input().split()]
m=x[0]
n=x[1]
Graph=[[i] for i in range(m)]
visited=[False for i in range(m)]
# print(Graph)
# print(visited)

for i in range(n):
	temp=[int(i) for i in input().split()]
	Graph[temp[0]].append(temp[1])
	Graph[temp[1]].append(temp[0])
	# print(Graph) # undirected
start=int(input())
# print(Graph)

if start>=m:
	print('0')
	exit()

count=0
stack=[start]
visited[start]=True
while len(stack)!=0:
	val=stack.pop()
	visited[val]=True
	count+=1
	# print(count,val)
	for i in Graph[val][1:]:
		if visited[i]==False:
			if stack.count(i)==0:
				stack.append(i)
# print(visited.count('True'))
print(count)
# def countNode(n,m,edges):->[]	



#TC v+e
#sc o(n)