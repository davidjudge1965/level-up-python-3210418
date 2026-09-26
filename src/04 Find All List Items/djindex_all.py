def indexofnumber(thelist, number, positionprefix):
    if isinstance(thelist, list):
        print(f'The parameter list is a list: {thelist}')
    else:
        # Must be a sole number then
        if thelist == number:
          return positionprefix + 1
    
def index_all2(mylist, number):
    print(f'Looking for {number} in list {mylist}')


def index_all(input_list, item):
    # input_list is the list to go through
    # item is the value to search for
    found_list = []
    # Enumerate the list so that for each item in the list you also get its index and not just the value (or list)
    for index, value in enumerate(input_list):
        if value == item:
            # When the value of the input_list at the current index is equal to the item we are searching for, 
            # append the index to the found_list
            found_list.append([index])   # add index as a list item to found_list
        elif isinstance(input_list[index], list):
            # If the element at index position of input_list is a list, then call the function recursively to search through that sublist
            for i in index_all(input_list[index], item):
                found_list.append([index] + i)   # add index as a list item to found_list
    return found_list

# commands used in solution video for reference
if __name__ == '__main__':
    print(index_all([2,[2,3]], 2))  
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print(index_all(example, 2))  # [[0, 0, 1], [0, 1], [1, 1]]