def freq_dict(string):
    """
    * string is a string
    Returns a dictionary of the frequency of words in string e.g. I like apples = {'i':1, 'like':1, 'apples':1}
    """
    freq_dict = {}
    Lstring = string.lower().split()
    for elem in Lstring:
        if elem not in freq_dict:
            freq_dict[elem] = 1
        else:
            freq_dict[elem] += 1
    return occurs_often(freq_dict, 3)

def most_occuring(freq_dict):
    """
    * freq_dict is a dictionary of strings with ints as values
    Returns the key with the highest value
    """
    words = []
    highest = max(freq_dict.values())
    for k,v in freq_dict.items():
        if v == highest:
            words.append(k)
    return (words, highest)

def occurs_often(freq_dict, x):
    """
    * freq_dict is a dictionary of strings with ints as values
    * x is an int
    Returns a tuple containing the keys of freq_dict sorted by their value if that value is greater than x
    """
    freq_list = []
    word_freq_tuple = most_occuring(freq_dict)
    while word_freq_tuple[1] >= x:
        word_freq_tuple = most_occuring(freq_dict)
        freq_list.append(word_freq_tuple)
        for word in word_freq_tuple[0]:
            del(freq_dict[word])
    return freq_list

string = 'I like apples I I I apples rah ro ro ro ro ro rah I apples like'
print(freq_dict(string))
