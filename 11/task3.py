def reverse_list(lst):
    """
     This function reverse list
     Args:
         list:   list
     Returns:
         reverse list
     Raises:
         AssertionError, ValueError
     Examples:
        <<<<[1, 2, 3, 4]
        [4, 3, 2, 1]
     """
    if len(lst) == 1:
        return lst
    else:
        divide = len(lst)//2
        return reverse_list(lst[divide:]) + reverse_list(lst[:divide])

lst = input('Enter the list: ').split()
print(reverse_list(lst))
