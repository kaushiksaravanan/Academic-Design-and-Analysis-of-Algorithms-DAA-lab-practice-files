vertex=4
adj_matrix=[[i] for i in range(vertex)]
edges=[]
edges=5
# for i in range(edges):
#     print('<start vertext> <end vertex> <distance>')
#     temp=[int(i) for i in input().split()]
#     edges.append([temp[0],temp[1],temp[2]])
# print(edges)
#sorting
#start index 0
edges=[
    (0,1,10),
    (1,3,15),
    (2,3,4),
    (2,0,6),
    (0,3,5)
]
#
sorted_edge=sorted(edges,key=lambda x:x[2])
dict={sorted_edge[0][0],sorted_edge[0][1]}
mst_edges=[sorted_edge[0]]
for i in sorted_edge[1::]:
    if i[0] in dict and i[1]  in dict:
        pass
    else: 
        mst_edges.append(i)
        dict.add(i[0])
        dict.add(i[1])
distance=0
for i in mst_edges:
    print(i[0],' to ',i[1])
    distance+=i[2]
print(distance)
