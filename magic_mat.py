#magic matrix
arr = [[4,3,8],[9,5,1],[2,7,6]]
# for i in arr:
#     print(i)
#     print(sum(arr[i][:]))
    
# for i,j in enumerate(arr):
#     print(i,j[-1:])

# Magic matrix
arr = [[4, 3, 8], [9, 5, 1], [2, 7, 6]]


column_sums = []


for j in range(len(arr[0])):
    
    column_sum = 0

   
    for i in range(len(arr)):
        
        column_sum += arr[i][j]

   
    column_sums.append(column_sum)


print(column_sums)