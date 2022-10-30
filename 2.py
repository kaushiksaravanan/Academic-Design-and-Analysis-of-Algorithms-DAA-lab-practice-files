n=int(input())
arr=[int(i) for i in input().split()]
c=0
# temp=arr[:]
ind_to_start=n
ind_to_end=0
curr_max=-99
for i in range(n):
	if curr_max<arr[i]:
		curr_max=arr[i]
	else:
		ind_to_start=min(i,ind_to_start)
		ind_to_end=max(i,ind_to_end)
#unsorted part
# arr[ind_to_start-1:ind_to_end+1]

for i in range(ind_to_start-1,ind_to_end+1):
		curr=arr[i]
		j=i-1
		while j>=0 and curr<arr[j]:
				arr[j+1]=arr[j]
				j-=1
		arr[j+1]=curr

print(ind_to_end+1-ind_to_start+1)
print(*arr)

#tc 0(unsorted_length^2)
#sc o(n)