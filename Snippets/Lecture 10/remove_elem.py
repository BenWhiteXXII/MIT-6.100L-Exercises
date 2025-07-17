def remove_elem(L, e):
    """
    * L is a list
    * e is an object
    Returns a new list with elements in the same order as L
    but without any elements equal to e
    """
    fL = []
    for i in L:
        if i != e:
            fL.append(i)
    return fL

L =[1,2,2,2]
print(remove_elem(L, 2))
