

def MaximumProfit(arr, t):
    arr.sort(key = lambda x: -x[2])
    n = len(arr)
    result = [False]*n
    job = [-1]*n
    print(*arr)
    for i in range(n):
        for j in range(min(n-1, arr[i][1]-1),-1,-1):
            if not result[j]:
                result[j] = True
                job[j] = arr[i][0]
                break
    print(*job)
arr=[]
for _ in range(int(input())):
    t=input().split()
    arr.append([t[0],int(t[1]),int(t[2])])
print(MaximumProfit(arr,3))