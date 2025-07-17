def sum_and_prod(*L):
    """
    * L is a list of numbers
    Return a tuple where the first value is the
    sum of all elements in L and the second value
    is the product of all elements in L
    """
    (sum_L, prod_L) = (0, 1)
    for i in L:
        sum_L += int(i)
        prod_L = prod_L * int(i)
    return (sum_L, prod_L)

print(sum_and_prod(1, 3, 4))
