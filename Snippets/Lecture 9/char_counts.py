def char_counts(s):
    """
    * s is a string of lowercase chars
    Returns a tuple where the first element is the
    number of vowels in s and the second element
    is the number of consonants in s
    """
    vow = 0
    con = 0
    for i in s:
        if i in ('a', 'e', 'i', 'o', 'u'):
           vow += 1
        else:
            con += 1
    return (vow, con)

print(char_counts(input("Enter a string: ")))
