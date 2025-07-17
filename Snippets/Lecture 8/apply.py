def apply(criteria,n):
    """
    * criteria is a func that takes in a number and returns a bool
    * n is an int
    Returns how many ints from 0 to n (inclusive) match the criteria
    (i.e. return True when run with criteria)
    """
    count = 0
    for i in range(n+1):
        if criteria(i) == True:
            count += 1
    return count

def is_even(x):
    return x % 2 == 0

print(apply(is_even,3))
