lst = []
element = ''
lenght = int(input('Enter the lenght of list: '))


def create_List(lenght):
    """
    This function creates a list

    Args :
        lenght: lenght of list

    Reterns:
        list
    """
    global lst
    global element
    if lenght < 1:
        return
    else:
        element = int(input('Enter the element of list: '))
        lst.append(element)
        return create_List(lenght-1)


create_List(lenght)
lst.sort()
count = 0


def equal_max(lst):
    """
    This function find an equal maximum elements in the list

    Args:
        lst: list

    Returns:
        amount of equal maximum elements
    Raises:
        ValueError, OverflowError, ZeroDivisionError
    """
    global count
    if len(lst) == 0:
        return count
    if len(lst) == 1:
        count += 1
        return
    if lst[-2] < lst[-1]:
        count += 1
        return
    else:
        count += 1
        return equal_max(lst[:-1])


equal_max(lst)
print(count)
