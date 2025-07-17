def make_ordered_list(n):
    """
    * n is a positive int
    Returns a list containing all ints in order
    from 0 to n (inclusive)
    """
    ints = []
    for i in range(n+1):
        ints.append(i)
    return ints

print(make_ordered_list(10))
