
def largest_element_array(arr):
    '''
    This function would return the 
    largest of all the elements.
    '''
    largest = float('-inf')

    for element in arr:
        if element > largest :
            largest = element
    
    return largest


# Use of the above function :-
print(largest_element_array([1,2,3,4,100,5,23,101]))
print(largest_element_array([1000, -1]))