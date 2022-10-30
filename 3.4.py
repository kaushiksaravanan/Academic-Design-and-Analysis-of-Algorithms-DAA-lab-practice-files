

arr=[int(i) for i in input().split()]
#break into array where we have a repeaded element
d={}
count=1
for i in arr:
    if i in d:
        count+=1
        d.clear()
        d[i]=1
    if i not in d:  
        d[i]=1
print(count)

#tc o(1)
#sc o(1)