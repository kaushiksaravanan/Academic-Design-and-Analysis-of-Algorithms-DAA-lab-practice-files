# n=int(input())
#arr=[]
# for i in range(n):
#     arr.append([int(i) for i in input().split()])
# w=int(input())
arr=[[60,10],[100,20],[120,30]]
w=50

arr.sort(key=lambda x: (x[0]/x[1]), reverse=True)

value=0
for i in arr:
    if i[1]<=w:
        w-=i[1]
        value+=i[0]
    else:
        value+=i[0]*w/i[1]
        break
print(value)

