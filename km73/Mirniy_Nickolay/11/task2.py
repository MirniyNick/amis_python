def minimum(lst, iterator):
    """
    This function find minimum in list
     Args:
         list:   list
         lenght:   lenght of list
     Returns:
         float number minimum in list
     Raises:
         ValueError
     """
    if len(lst) == 0:
        return
    elif len(lst) == 1:
        return lst
    maximum = max(lst)
    lst.remove(maximum)
    return minimum(lst, iterator-1)

lst = input('Enter the list: ').split()
print(minimum(lst, len(lst)))
