def all_true(n, Lf):
    """ n is an int
        Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called
    with n as a parameter. Otherwise returns False.
    """
    # Your code here
    for f in Lf:
        if not f(n):
            return f(n)
    return True

# def func_a(n):
#     if n == 5:
#         return True
#     else:
#         return False

# def func_b(n):
#     if n == 6:
#         return True
#     else:
#         return False
# Examples:
print(all_true(6, [func_a, func_b]))
