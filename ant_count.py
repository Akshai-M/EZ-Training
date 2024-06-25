def ant(A):
    current_position = 0
    count = 0

    for move in A:
        current_position+=move
        if current_position == 0:
            count+=1
        
    return count

ant(10)