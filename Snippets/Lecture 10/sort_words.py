def sort_words(sen):
    """
    * sen is a string representing a sentence
    Returns a list containing all the words in sen but
    sorted in alphabetical order
    """
    return sorted(sen.split(' '))

print(sort_words("look at this photograph"))
