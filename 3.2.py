# 6
# 3 10 16 13 5 5
# 21
#two sum


n=int(input())
arr=[int(i) for i in input().split()]
target=int(input())
d=dict()

ind=0
for i in arr:
    d[i]=ind
    ind+=1
print(d)

possible_pairs=[0,0]
max_diff=0
for i in arr:      
    if target-i in d:
        curr_diff=i-target+i
        if max_diff<curr_diff:
            possible_pairs=[i,target-i]
            max_diff=curr_diff

print(str(possible_pairs[0])+','+str(possible_pairs[1]))
