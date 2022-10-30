n=int(input())
arr=[]
for i in range(n):
	temp=input().split()
	arr.append([int(i) for i in temp[0].split('/')]+[int(temp[1])])
# print(arr)

def compare_arr(a,b):
	#same date larger no
	if a[2]==b[2] and a[1]==b[1] and a[0]==b[0] and a[3]<b[3]:
		return True
	#same year n month but larger data
	if a[2]==b[2] and a[1]==b[1] and a[0]<b[0]:
		return True
	#same year but larger month
	if a[2]==b[2] and a[1]<b[1]:
		return True
	#larger year
	if a[2]<b[2]:
		return True
	return False
		

for i in range(n):
	curr_ind=i
	curr_min=arr[i]
	ele=0
	for min_ind in range(i+1,n):
		if compare_arr(arr[min_ind],curr_min):
			curr_min=arr[min_ind]
			curr_ind=min_ind
	temp=arr[i]
	arr[i]=arr[curr_ind]
	arr[curr_ind]=temp
print()
for i in arr:
	t=[]
	for ch in i[:3]:
		m=str(ch)
		if len(m)==1:
			val='0'+m
		else:
			val=m
		t.append(val)
	print("/".join(t),i[3])