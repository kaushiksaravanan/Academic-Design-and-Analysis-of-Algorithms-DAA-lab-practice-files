arr=[
    ('a',2,100),
    ('b',1,19),
    ('c',2,27),
    ('d',1,25),
    ('e',3,15)
    ]
arr_sort=sorted(arr,key=lambda x:x[2])
arr_sort=arr_sort[::-1]
result_seq=[arr_sort[0]]
print(arr_sort)
n=len(arr)
curr=0
for i in range(curr,n):
    pass
