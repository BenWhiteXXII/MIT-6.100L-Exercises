def remove_all(L, e):
    """
    * L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None
    """
    # Ln = L[:]
    # L.clear()
    # for i in Ln:
    #     if i != e:
    #         L.append(i)
    # return None
    while e in L:
        L.remove(e)
    return None

Lin =[1,2,2,2]
remove_all(Lin, 2)
print(Lin) # prints [1]
