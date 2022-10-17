# val=[]
# def recur_sum_back(index,req,arr,curr_arr):
#     r=sum(curr_arr)
#     if r>req:
#         return False
#     # print(curr_arr)
#     if sum(curr_arr)==req:
#         val.append(curr_arr[:])
#     if index>=len(arr):
#         return False
#     curr_arr.append(arr[index])
#     recur_sum_back(index+1,req,arr,curr_arr)
#     curr_arr.remove(arr[index])
#     recur_sum_back(index+1,req,arr,curr_arr)
# recur_sum_back(0,15,[3,5,6,7],[])
# print(val)

x=[0]*4
val=[]
def btrack(i,n,s,r,elements,m,x):
    if i<n:
        print(x)
        # if s+elements[i]==m:
        #     print(x)
        #     val.append(x[:])
        # if s+elements[i]==m:
        #     # print(x)
        #     x[i]=1
        #     val.append(x[:])
        #     return
            # btrack(i+1,n,s+elements[i],r-elements[i],elements,m,x)


        x[i]=1
        if s+elements[i]<=m:
            btrack(i+1,n,s+elements[i],r-elements[i],elements,m,x)
        x[i]=0
        if s+elements[i]>=m:
            btrack(i+1,n,s,r-elements[i],elements,m,x)
        
        
btrack(0,4,0,10,[3,5,6,7],15,x)
print(val)