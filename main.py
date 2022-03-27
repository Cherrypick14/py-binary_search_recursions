#recursive implementation of binary search in python
#performing recursive binary search of an integer in a sorted list

def recursive_binary_search(c_list,item):
    
    first = 0
    last = len(c_list-1)
    if len(c_list) == 0:
        return "it's not in the list".format(item=item)
    else:
        i = (first + last)//2
    if item == c_list[1]:
           return "was found in the list".format(item=item)
    else:
        if c_list[i] < item:
         return recursive_binary_search(c_list[i+1:],item)
        else:
         return recursive_binary_search(c_list[:i],item)

#recursive_binary_search([2,5,6,7],6)
