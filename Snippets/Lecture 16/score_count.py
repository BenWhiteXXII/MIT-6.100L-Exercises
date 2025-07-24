def score_count(x):
    """
    Returns all the ways to make a score of x by adding
    1, 2, and/or 3 together. Order doesn't matter.
    """
    if x in scores:
        return scores[x]
    else:
        accum = score_count(x-1) + score_count(x-2) + score_count(x-3)
        scores[x] = accum
        return accum

scores = {1:1, 2:2,  3:3}
print(score_count(84))
