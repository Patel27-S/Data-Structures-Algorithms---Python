

def min_heapify(list, index):

    # First thing that we will do is
    # find out the smallest of list[index]
    # , list[2*index +1], list[2*index +2]
    smallest = None

    if list[index] > list[2*index +1]:
        smallest = list[2*index +1]
    else:
        smallest = list[index]
    if smallest > list[2*index +2]:
        smallest = list[2*index +2]
    
    # Now we have smallest value stored in smallest variable. Hence, 
    # the first thing we will do is check if smallest is equal 
    # to the value of node itself,(i.e. the list[index]), if it is so, 
    # then we have to do absolutely nothing. Hence;
    if smallest == list[index]:
        return
    # Else, if the either of the children have the smaller values, then 
    # we swap the values of root/index with that particular child, and then 
    # run min_heapify() over that child as well. :
    elif smallest == list[2*index +1]:
        list[index], list[2*index +1] = \
            list[2*index +1], list[index]
        min_heapify(list, 2*index +1)
    else:
        list[index], list[2*index +2] = \
            list[2*index +2], list[index]
        min_heapify(list, 2*index +2)
        

def build_heap(list):
    # To build the heap, we have a very simple logic. We'll basically 
    # run min_heapify() from the first parent to the root parent :

    # Below denotes the first parent of the list:
    i = (len(list) -1)//2

    # From the first parent of the list to the last parent which is the root we have to run the min_heapify function;
    while i:
        min_heapify(list,i)
        i = i//2
    
    # we return the list which represents a min_heap.
    return list


result = build_heap([1,4561,55, 78, 77, 898])
print(result)