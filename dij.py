g=[
    [0,7,False,False,False,False,False,2,False,False],
    [7,0,4,1,False,5,False,False,False,False],
    [False,4,0,False,False,False,False,8,False,False],
    [False,1,False,0,6,8,3,3,False,False],
    [False,False,False,6,0,False,False,6,8,False],
    [False,5,False,8,False,0,False,False,False,False],
    [False,False,False,3,False,False,0,False,9,2],
    [2,False,8,3,6,False,False,0,False,False],
    [False,False,False,False,8,False,9,False,0,False],
    [False,False,False,False,False,False,2,False,False,0]
]
temp={}
for i in range(len(g)):
    temp[i]=float("inf")
dist=[float("inf")]*len(g)
temp[0]=0
while len(temp)>0:
    min_v=min(temp.values())
    min_k=min(temp,key=temp.get)
    temp.pop(min_k)
    dist[min_k]=min_v
    for j in range(len(g)):
        if g[min_k][j]!=False and g[min_k][j]!=0: 
            new_dist=min_v+g[min_k][j]
            if j in temp.keys() and temp[j]>new_dist:
                temp[j]=new_dist
print(dist)