def is_triangular(n):
    """
    n is a int > 0
    Returns True if n is triangular, i.e. equals a continued
    summation of natural number (1+2+3...+k), False otherwise.
    """
    total = 0
    for i in range(n+1):
        total += i
        if total == n:
            return True
    return False

print(is_triangular(int(input('Enter no.: '))))
