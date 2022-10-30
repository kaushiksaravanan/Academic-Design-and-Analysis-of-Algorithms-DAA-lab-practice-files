def four_1():
	temp=input().split()
	pattern=temp[0]
	text=temp[1]
	start=0
	while len(pattern)<len(text):
		
		if len(pattern)<=start:
			break
		flag=0
		for i in range(len(pattern)):
			if flag==1:
				break
			if pattern[i]!=text[i+start]:
				flag=1
		if i==1:
			i=1
		else:
			i+=1
		start=i+start 

	flag=0
	print(start)
	if len(pattern)==len(text[start:]) and text[start:]==pattern: 
		return 'YES'
	else:
		return 'NO'
for _ in range(int(input())):
	print(four_1())