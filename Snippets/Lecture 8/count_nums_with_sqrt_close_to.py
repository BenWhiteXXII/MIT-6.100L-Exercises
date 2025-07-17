def count_nums_with_sqrt_close_to (n, epsilon):
    """
    n is an int > 2
    epsilon is a postive number < 0
    Returns how many integers have a square root within epsilon of n
    """
    count = 0
    for x in range(n**3):
        # take sqrt of x
        low = 0
        high = x
        ans = (high + low) / 2.0
        while abs(ans**2 - x) >= epsilon:
            if ans**2 < x:
                low = ans
            else:
                high = ans
            ans = (high + low) / 2.0
        # sqrt is within epsilon
        if abs(n - ans) <= epsilon:
            count += 1
            # break early once in appropriate range i.e we have all possible integers
            if ans**2 > (n + epsilon)**2:
                break
    return(count)

print(count_nums_with_sqrt_close_to(10, 0.1))
