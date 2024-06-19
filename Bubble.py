l = list(map(int, input().split()))
n = len(l)
for i in range(n-1):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print(l)