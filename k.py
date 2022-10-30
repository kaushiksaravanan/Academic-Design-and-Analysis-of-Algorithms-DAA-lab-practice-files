n=int(input())
arr=[int(i) for i in input().split()]
for i in range(n):
	for j in range(n):
		if arr[i]>arr[j]:
			temp=arr[i]
			arr[i]=arr[j]
			arr[j]=temp
print(arr)