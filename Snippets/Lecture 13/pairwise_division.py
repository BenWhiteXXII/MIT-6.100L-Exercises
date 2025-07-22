def pairwise_div(Lnum, Ldenom):
    """
    * Lnum and Ldenom are non-empty lists of equal lengths containing numbers.
    Returns a new list whose elements are the pairwise
    divisions of an element in Lnum by an element in Ldenom.

    Raise a ValueError if Ldenom contains 0.
    """
    assert len(Lnum) == len(Ldenom), "List lengths differ"
    assert len(Lnum) != 0 and len(Ldenom) != 0, "Empty list"
    try:
        Ldiv = [Lnum[i] / Ldenom[i] for i in range(len(L1))]
        return Ldiv
    except ZeroDivisionError:
        raise ValueError('List contains 0')

# examples
L1 = [4,5,6]
L2 = [1,2,3]
# print(pairwise_div(L1, L2)) # prints [4.0,2.5,2.0]

L1 = [4,5,6]
L2 = [1,0,3]
# print(pairwise_div(L1, L2)) # raises a ValueError

L1 = []
L2 = [1,0,3]
print(pairwise_div(L1, L2)) # raises an AssertionError
