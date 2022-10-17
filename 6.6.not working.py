start=[10,20,30]
end=[20,25,30]
combined=[]
for i in range(len(start)):
    #start,finish,job_no
    combined.append((start[i],end[i],i))

#o(nlogn)
combined_sorted=sorted(combined,key=lambda x:x[1])
# print(combined_sorted)
#directly adding the first job
jobs=[combined_sorted[0]]
recent_job=combined_sorted[0]
curr=0
while curr<=len(start):
    for i in range(curr+1,len(start)):
        if recent_job[1]<combined_sorted[i][0]:
            jobs.append(combined_sorted[i])
            recent_job=combined_sorted[i]
            curr=i
        else:
            pass
    curr+=1
for i in jobs:
    print(i[2],end=' ')

#TC O(n^2) sorting nlogn + n^2 (when all overlaps)
#SC O(n) output array

