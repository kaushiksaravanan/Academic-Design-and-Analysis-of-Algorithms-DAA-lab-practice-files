arr=[1, 2, 5, 10, 20, 50, 100, 500, 1000][::-1]
n=int(input())
# n=121
print(n)
d={}
while n>0:
    for i in arr:
        if n-i>=0:
            n=n-i
            if i in d:
                d[i]+=1
            if i not in d:
                d[i]=1
            break
count=0
for i in d:
    count+=d[i]
print(count)

            
    