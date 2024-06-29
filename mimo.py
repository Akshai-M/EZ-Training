def cost(curr,v,g,dp):
    n=len(g)
    if len(v)==n:
        return g[curr][0]
    visit=tuple(v)
    if (curr,visit) in dp:
        return dp[(curr,visit)]
    mini=float("inf")
    for i in range(n):
        if i not in v:
            new_v=v+[i]
            new_cost=g[curr][i]+cost(i,new_v,g,dp)
            mini=min(mini,new_cost)
    dp[(curr,visit)]=mini
    return mini


g=[
    [0,4,7,5,5],
    [4,0,2,3,8],
    [7,2,0,3,4],
    [5,3,3,0,6],
    [5,8,4,6,0]
]
n=len(g)
dp={}
print("Minimum cost:",cost(0,[0],g,dp))