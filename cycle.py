x=[int(i) for i in input().split()]
m=x[0]
n=x[1]
Graph=[[i] for i in range(m)]

for i in range(n):
	temp=[int(i) for i in input().split()]
	Graph[temp[0]].append(temp[1])
V=m
visited=[0]*V
recStack=[0]*V
def check():
		def isCyclicUtil(v):
			visited[v]=True
			recStack[v]=True
			for neighbour in Graph[v][1:]:
				if visited[neighbour]==0:
					if isCyclicUtil(neighbour)==True:
						return True
				elif recStack[neighbour]==True:
					return True
			recStack[v]=0
			return False                                    

		for node in range(V):
			if visited[node]==0:
				if isCyclicUtil(node)==True:
					return True
		return False
print(check())

#TC v+e
#sc o(v)
