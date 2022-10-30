adj_mat=[]
v=int(input("Enter no of vertices - n\n"))
k=int(input("No of pairs to remove - k\n"))

#adjacency matrix intitalization
for i in range(v):
	temp=[]
	for i in range(v):
		temp.append(1)
	adj_mat.append(temp)
to_rem=[i for i in range(v,v-k,-1)]

#finding vertices's edges to remove
for i in to_rem:
	if i<=1:
		print(-1)
		exit()
# print(to_rem)
print()

for i in range(k):
	for j in range(i+1,k):
			print('({i},{j})'.format(i=to_rem[i],j=to_rem[j]))
			adj_mat[to_rem[i]-1][to_rem[j]-1]=0
			adj_mat[to_rem[j]-1][to_rem[i]-1]=0

print()
print('adjacency matrix final')
for i in range(v):
	for j in range(v):
		if i==j:
			print(0,end=' ')  #no self loop considered
		else:
			print(adj_mat[i][j],end=' ')
	print()


#TC O(k^2) # excluding input and output
#SC O(v*v) # for adjacency matrix