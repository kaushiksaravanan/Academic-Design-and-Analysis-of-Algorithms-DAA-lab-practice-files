arr= [9.00,  9.40, 9.50,  11.00, 15.00, 18.00]
dep= [9.10, 12.00, 11.20, 11.30, 19.00, 20.00]
x=[]
for i in arr:
    x.append((i,'a'))
for i in dep:
    x.append((i,'d'))
ans_s=sorted(x,key=lambda x:x[0])
print(ans_s)
curr=0
glob_max=-9999
for i in ans_s:
    if i[1]=='d':
        curr-=1
    if i[1]=='a':
        curr+=1
    glob_max=max(glob_max,curr)
print(glob_max)