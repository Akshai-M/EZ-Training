def bellmanford(V,edges):
    a='ABCDEF'
    d={}
    d=d.fromkeys(a,float('inf'))
    print(d)
    
    d['A']=0
    for _ in range(V-1):
        for u,v,wt in edges:
        # print(u,v,wt)
            if d[u]!=float('inf') and d[u]+wt<d[v]:
                d[v]=d[u]+wt
            print(d)
if __name__ == "__main__":
    V = 6
    edges = [
        ('A','B',6),
        ('A','C',4),
        ('A','D',5),
        ('B','E',-1),
        ('C','B',-2),
        ('C','E',3),
        ('D','C',-2),
        ('D','F',-1),
        ('E','F',3)
    ]
    bellmanford(V,edges)