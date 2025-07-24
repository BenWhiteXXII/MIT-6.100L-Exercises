def fibonacci(n):
    """
    * n is a non-zero integer
    Returns the nth value of the fibonacci sequence
    """
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
