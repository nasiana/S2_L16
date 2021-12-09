"""
EXAMPLE SOLUTION FOR 3 LARGEST NUMBERS WITHOUT SORTING

Check test cases below to test your code
"""

### ADD YOUR CODE HERE ###


#########################################################################

# Case 1, result = [18, 141, 541]



def find_3_largest_nums(iterable):
    array = iterable.copy()
    max_len = 3
    while len(array) > max_len:
        for i in array:
            if i == min(array):
                array.remove(i)
    max_num = max(array)
    min_num = min(array)
    array_2 = []
    if max_num != min_num:
        array.remove(max_num)
        array.remove(min_num)
    else:
        array = min_num
    array_2.append(min_num)
    array_2.append(array)
    array_2.append(max_num)
    return array_2


array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(find_3_largest_nums(array))

#####################################################

# Case 2, result = [8, 8, 10]
array = [8, 8, 8, 8, 8, 8, 8, 8, 10, 8, 8, 8, 8, 8]
print(find_3_largest_nums(array))

#####################################################

# Case 3, result = [1, 1, 1]
array = [1, 1, 1, 1, 1, 1, 1, 1]
print(find_3_largest_nums(array))

####################################################

# Case 4, result = [-2, -1, 7]
array = [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]
print(find_3_largest_nums(array))

####################################################