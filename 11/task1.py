lst = []
element = ''
lenght = int(input('Enter the lenght of list: '))


def createList(lenght):
    """
    This function creates list

    Args:
        lenght: lenght of list

    Returns:
        list
    Raises:
        AssertionError, ValueError
    Examples:
        <<<< lenght = 4
        [1, 2, 0, 2]
    """
    global lst
    global element
    if lenght < 1:
        return
    else:
        element = int(input('Enter the element of the list: '))
        lst.append(element)
        return createList(lenght-1)


createList(lenght)
counter = 2


def replace_zero(lst, lenght):
    """
    This function replaces every zero in list in summa of two previous elements

    Args:
        lst: list
        lenght: lenght of list
    Returns:
        List without zeroes
    Raises:
        AssertionError, ValueError
    Examples:
        <<<<[1, 2, 0, 2]
        [1, 2, 3, 2]
    """
    global counter
    if lenght == 2:
        return
    if len(lst) < 3:
        return lst
    if lst[counter] == 0:
        lst[counter] = lst[counter-1] + lst[counter-2]
        counter += 1
        return replace_zero(lst, lenght-1)
    else:
        counter += 1
        return replace_zero(lst, lenght-1)


replace_zero(lst, lenght)
print(lst)
