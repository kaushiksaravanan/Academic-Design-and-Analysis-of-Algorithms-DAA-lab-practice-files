def mergesort(arr):
	if len(arr)>=0:
		mid=len(arr)//2
		L=arr[:mid]
		R=arr[mid:]
		mergesort(L)
		mergesort(R)
		i=0
		j=0
		k=0
		while i<len(L) and j<len(R):
			if L[i][1]<=R[j][1]:
				arr[k]=L[i]
				i+=1
			else:
				arr[k]=R[j]
				j+=1
			k+=1
		while i<len(L):
			arr[k]=L[i]
			i+=1
			k+=1
		while j<len(R):
			arr[k]=R[j]
			j+=1
			k+=1
	else:
		return
arr=[]
n=int(input())
for i in range(n):
	k=input().split()
	arr.append([k[0],int(k[1])])
mergesort(arr)
for i in arr:
	print(i[0],end=' ')