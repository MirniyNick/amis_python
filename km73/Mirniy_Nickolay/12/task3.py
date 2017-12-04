def groups(list, ind=0, group=1, max_group=1):
    """
    This function finds the group with the biggest amount of equal numbers

    Args:
        list: list
        ind: index
        group , max_group: constant

    Returns:
        The amount of equal numbers in the biggest group

    Example:
        >>>[2, 3, 3, 3, 3, 1]
        4
    """
    if ind == len(list) - 1:
        return max_group
    elif list[ind] == list[ind + 1]:
        group += 1
        if max_group < group:
            max_group = group
    else:
        group = 1
    return groups(list, ind + 1, group, max_group)


lst = input("Sequence of numbers: ").split()
print(largest_group(lst))
