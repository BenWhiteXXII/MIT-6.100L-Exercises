def total_len_recur(L):
    """
    * L is a list of strings
    Returns the total length of all strings
    """
    if len(L) == 1:
        return len(L[0])
    else:
        return len(L[0]) + total_len_recur(L[1:])

test = ['ab', 'c', 'defgh']
print(total_len_recur(test)) # prints 8
