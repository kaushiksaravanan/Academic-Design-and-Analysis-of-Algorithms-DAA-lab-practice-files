x=[int(i) for i in input().split()]
m=x[0]
n=x[1]
Graph=[[i] for i in range(m)]
visited=[False for i in range(m)]

for i in range(n):
	temp=[int(i) for i in input().split()]
	# print(temp)
	Graph[temp[0]-1].append(temp[1]-1)
	# Graph[temp[1]-1].append(temp[0]-1)
print(Graph)
t=[int(i) for i in input().split()]
no_pas=t[2]
start=t[0]
end=t[1]


c=0
l=0
count=[]
if True:
	stack=[start]
	visited[start]=True
	while len(stack)!=0:
		val=stack.pop()
		# if val==no_pas:
			# continue
		visited[val]=True
		count.append(val)
		for i in Graph[val][1:]:
			if visited[i]==False:
				if stack.count(i)==0:
					# if i==no_pas:
					# 	continue
					stack.append(i)
	if count==m:
		c+=1
	l+=1
# if c==l:
# 	print('YES')
# else:
# 	print('NO')
print(count)
if no_pas in count:
	print('NO')
else:
	print('YES')