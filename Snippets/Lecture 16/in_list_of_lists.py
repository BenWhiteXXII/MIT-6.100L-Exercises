def in_list_of_lists(L, e):
    """
    * L is a list whose elements are lists containing ints.
    Returns True if e is an element within the lists of L
    and False otherwise.
    """
    if len(L) == 1:
        return e in L[0]
    else:
        if e in L[0]:
            return True
        else:
            return in_list_of_lists(L[1:], e)

test = [[1,2], [3,4], [5,6,7]]
print(in_list_of_lists(test, 0)) # prints False
print(in_list_of_lists(test, 3)) # prints True
