def break_words(stuff):
    """This function will break up the words."""
    words = stuff.split()
    return words

def sort_words(stuff):
    """Sort the words"""
    return sorted(stuff)

def print_first_word(stuff):
    """Prints the first word after popping it off"""
    word = stuff.pop(0)
    print(word)

def print_last_word(stuff):
    """Prints the last word"""
    word = stuff.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes full sentence and returns the words"""
    words = break_words(sentence)
    return sorted(words)

def print_first_and_last(sentence):
    """Prints the first and last word of the sentence"""
    words = break_words(sentence)
    #first = words.pop(0)
    #last = words.pop(-1)
    #return first , last
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Prints the first and last words after sorting the sentence"""
    sorted = sort_sentence(sentence)
    print_first_word(sorted)
    print_last_word(sorted)
