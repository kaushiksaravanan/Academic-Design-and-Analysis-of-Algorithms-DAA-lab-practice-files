
vertices=4
n=4
graph=[[0 for __ in range(vertices)]for _ in range(vertices)]
colour=[0]*vertices
def isSafe(row,c):
		for i in range(vertices):
			if graph[row][i]==1 and colour[i]==c:
				return False
		return True
def graph_col(i,m):
    if i!=n:
        for j in range(1,m+1):
            if isSafe(i,j):
                colour[i]=j
                graph_col(i+1,m)


graph=[[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]]
m=3
graph_col(0,m)
n1=len(set(colour))
if m<=n1:
    print('Yes')
else:
    print('No')
print(*colour)
