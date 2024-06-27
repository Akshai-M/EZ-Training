def merge(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    lefthalf=arr[:mid]
    righthalf=arr[mid:]
    left_sort=merge(lefthalf)
    right_sort=merge(righthalf)
    return merge_sort(left_sort,right_sort)

def merge_sort(left,right):
    l=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1
    l.extend(left[i:])
    l.extend(right[j:])

    return l
arr=list(map(int, input().split()))
print(arr)
print(merge(arr))