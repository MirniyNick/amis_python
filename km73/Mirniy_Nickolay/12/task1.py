lenght = int(input('Enter the lenght of list: '))
lst = []
element = ''


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


def second_max(lst):
    """
    This function find second maximum i list
    Args:
        list: list
    Returns:
        maximum: integer, result of the program
    Raises:
        ValueError, OverflowError, ZeroDivisionError
    """
    if len(lst) == 1:
        return lst
    elif lst[-2] < lst[-1]:
        return lst[:-1]
    else:
        return second_max(lst[:-1])


lst = second_max(lst)
print(lst[-1])
