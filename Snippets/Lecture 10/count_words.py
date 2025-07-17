def count_words(sen):
    """
    * sen is a string representing a sentence
    Returns how many words are in s (i.e. a word is a
    sequence of characters between spaces.
    """
    return len(sen.split(' '))

print(count_words("Hello it's me"))
