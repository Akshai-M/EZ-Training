arr = list(map(int, input().split()))
l =len(arr)

max = min = arr[0]
for i in range(0,l):
    
    if min >arr[i] :
        min = arr[i]
    elif max > arr[i]:
        max = arr[i]
print(min)
print(max)

