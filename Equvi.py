# matrix = [
#     [1, 2, 3, 4],
#     [5, 9, 2, 8],
#     [3, 5, 4, 2]
# ]

# target_value = 2
# indices = []

# for i, row in enumerate(matrix):
#     for j, element in enumerate(row):
#         if element == target_value:
#             indices.append([i, j])
        
# print(indices)


matrix = [
    [1, 2, 3, 4],
    [5, 9, 2, 8],
    [3, 5, 4, 2]
]

target_value = 2

# Function to find the sums to the left and right of the target value in a matrix
def find_sums(matrix, target_value):
    for row in matrix:
        print(row)
        if target_value in row:
            index = row.index(target_value)
            left_list = row[:index]
            right_list = row[index+1:]
            left_sum = sum(left_list)
            right_sum = sum(right_list)
            return left_sum, right_sum

# Find the sums for the target value
left_sum, right_sum = find_sums(matrix, target_value)

print("Left sum:", left_sum)
print("Right sum:", right_sum)
