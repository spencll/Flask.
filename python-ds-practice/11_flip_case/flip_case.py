def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    str = ''
    for letter in phrase:
        if letter.upper()== to_swap.upper():
            str = str+ letter.swapcase()
        else:
            str = str + letter
    return str
