def count_matches(d):
    """
    * d is a dict
    Returns how many entries in d have the key equal to its value
    """
    # count = 0
    # Ld = list(d.items())
    # for i in range(len(Ld)):
    #     if Ld[i][0] == Ld[i][1]:
    #         count += 1
    # return count
    count = 0
    for v,k in d.items():
        if v == k:
            count += 1
    return count
d = {1:2, 3:4, 5:6}
print(count_matches(d)) # prints 0

d = {1:2, 'a':'a', 5:5}
print(count_matches(d)) # prints 2
