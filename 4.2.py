from cmath import inf
def lps(strin):
	n=len(strin)
	lps_array=[0]*n
	for i in range(1,n+1):
		k_max=0
		k=0
		temp_string=strin[:i] #o(n)
		n_temp=len(temp_string)
		# print(temp_string,'<-')
		for ind in range(0,n_temp-1):
			# print(temp_string[:ind+1],temp_slps_pattern[matched]tring[-ind-1:],k_max)
			if temp_string[:ind+1]==temp_string[-ind-1:]:
				# print(ind)
				k_max=max(k_max,ind+1)
		lps_array[i-1]=k_max
		k_max=0
	return lps_array
# print(lps('abcab'))

def kmp(pattern,text):
	lps_pattern=lps(pattern)
	# print(lps_pattern)
	shift=0
	start=0
	while start+len(pattern)<=len(text):
		flag=0
		matched=0
		# print(pattern,text[start:])
		for i in range(len(pattern)):
			if flag==1:
				break
			if pattern[i]!=text[i+start]:
				flag=1
			matched+=1
		# print(pattern,text[start:])
		
		matched-=1
		if flag==0:
			return 'YES'
		# print(start,matched,lps_pattern[matched-1])
		# print(pattern,text[start:])

		start=start+matched-lps_pattern[matched-1]
		# if pattern==text[start:]:
		# 	return 'YES'
	return 'NO'
# print(kmp('ABABC','ABABABCABA'))
for _ in range(int(input())):
	temp=input().split()
	print(kmp(temp[0], temp[1]))