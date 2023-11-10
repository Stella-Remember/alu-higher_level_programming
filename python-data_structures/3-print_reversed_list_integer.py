#!/usr/bin/python3
<<<<<<< HEAD
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return ''
    else:
        my_list.reverse()
        length = len(my_list)
        for i in range(length):
            print("{:d}".format(my_list[i]))
=======
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
    return my_list
>>>>>>> 2b7df0b976f245c1ca7de9998bdfa0e52f2b06fd
