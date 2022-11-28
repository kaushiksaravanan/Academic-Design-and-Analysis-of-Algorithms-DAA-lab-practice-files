points=((2,10,'a1'),(2,5,'a2'),(8,4,'a3'),(5,8,'b1'),(7,5,'b2'),(6,4,'b3'),(1,2,'c1'),(4,9,'c2'))
c1=[(2,10)]
c2=[(5,8)]
c3=[(1,2)]
clu1=[c1[0]]
clu2=[c2[0]]
clu3=[c3[0]]
print()
def k_means(clu1,clu2,clu3,c1,c2,c3,c=1):
    while True:
        t_c_1=[]
        t_c_2=[]
        t_c_3=[]
        for i in points:
            d1=((c1[0][0]-i[0])**2+(c1[0][1]-i[1])**2)**0.5
            d2=((c2[0][0]-i[0])**2+(c2[0][1]-i[1])**2)**0.5
            d3=((c3[0][0]-i[0])**2+(c3[0][1]-i[1])**2)**0.5
            get_min=min(d1,d2,d3)
            if get_min==d1:
                t_c_1.append(i)
            if get_min==d2:
                t_c_2.append(i)
            if get_min==d3:
                t_c_3.append(i)
        if t_c_1==clu1 and t_c_2==clu2 and t_c_3==clu3:
            break
        else:
            clu1[:]=t_c_1
            clu2[:]=t_c_2
            clu3[:]=t_c_3
            print('Iteration '+str(c))
            print(*clu1,'center',*c1)
            print(*clu2,'center',*c2)
            print(*clu3,'center',*c3)   
            print('----------------')
            print() 
            new_mean_c1_x=sum([i[0] for i in c1])/len(c1)
            new_mean_c1_y=sum([i[1] for i in c1])/len(c1)
            new_mean_c2_x=sum([i[0] for i in c2])/len(c2)
            new_mean_c2_y=sum([i[1] for i in c2])/len(c2)
            new_mean_c3_x=sum([i[0] for i in c3])/len(c3)
            new_mean_c3_y=sum([i[1] for i in c3])/len(c3)
            c1=[(new_mean_c1_x,new_mean_c1_y)]
            c2=[(new_mean_c2_x,new_mean_c2_y)]
            c3=[(new_mean_c3_x,new_mean_c3_y)]
    c+=1
k_means(clu1,clu2,clu3,c1,c2,c3)
print('Answer')
print(*clu1,'center',*c1)
print(*clu2,'center',*c2)
print(*clu3,'center',*c3)     

    