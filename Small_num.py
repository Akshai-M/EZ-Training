def mini(arr):
   
    positive_numbers = [x for x in arr if x > 0]
    
    
    if not positive_numbers:
        return None  
    else:
        return min(positive_numbers)
arr = [3,4,-1,1]

print(mini(arr))