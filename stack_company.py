def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []
    
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        if stack:
            result[i] = stack[-1]
        
        stack.append(arr[i])
    
    return result

arr = [3, 5, 2, 14, 5, 3, 7, 9, 4, 6, 9, 4, 2, 5, 3]
output = next_greater_element(arr)
print(output)
