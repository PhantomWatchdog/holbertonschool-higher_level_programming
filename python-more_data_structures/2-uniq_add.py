#!/usr/bin/python3
def uniq_add(my_list=[]):
    ''' uniq_int = set()

    for num in my_list:
        uniq_int.add(num)

    total_sum = sum(uniq_int)

    return total_sum
    '''
    return sum(set(my_list))
