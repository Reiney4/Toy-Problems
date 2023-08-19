   #create a function positive_count with three arguments

def positive_count(a, b, c):
   
   
    # The function returns True if at least two of the arguments are positive
    
    positive_nums = [num for num in (a, b, c) if num > 0]
    
    if len(positive_nums) >= 2:
        return True
    #otherwise returns false
    else:
        return False


result = positive_count(10, -5, 2)
print(result)  

