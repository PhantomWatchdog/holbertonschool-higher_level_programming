#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides elements of two lists and return a new list with the results.

    Args:
        my_list_1 (list): First list of numbers.
        my_list_2 (list): Second list of numbers.
        list_length (int): Length of the lists.

    Return:
        list: New list containing the results of the division.

    Raise:
        None.

    """
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
