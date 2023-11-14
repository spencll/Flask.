def print_upper_words(words, *starting_letter):
    """Takes list of words and returns all caps on words with specified starting letter"""
    for word in words:
        if word.startswith(starting_letter):  
            print(word.upper()) 
