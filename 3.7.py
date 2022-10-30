
def max_pts(arr):
    dict_slope={}
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
                x1,y1=arr[i]
                x2,y2=arr[j]
                if x2-x1!=0:
                    slope=(y2-y1)/(x2-x1)
                    # print(arr[i],arr[j],slope)
                    if slope in dict_slope:
                        dict_slope[slope]+=1
                    if slope not in dict_slope:
                        dict_slope[slope]=1
    # for i in dict_slope:
    #     print(i,dict_slope[i])
    x=(sorted(dict_slope,key=lambda l:dict_slope[l]))[::-1]
    # print(gcd(2,6))
    max_slope=dict_slope[x[0]]
    # print(dict_slope)
    i=1
    while max_slope>0:
        max_slope-=i
        i+=1
    print(i)
    # print(sorted(slope,key=lambda l:dict_slope[l]))
max_pts([[-1,1],[0,0],[1,1],[2,2],[3,3],[3,4]])

#tc o(n^2)
#sc o(n) dict 