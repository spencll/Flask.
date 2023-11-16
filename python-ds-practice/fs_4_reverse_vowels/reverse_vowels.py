def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = 'aeiouAEIOU'
    vowel_order = []
    copy = s
    for letter in s:
        if letter in vowels:
            vowel_order.append(letter)
            copy = copy.replace(letter, '@', 1)
    vowel_order.reverse()
    for letter in copy:
        if letter=='@':
            copy = copy.replace('@',vowel_order[0],1)
            vowel_order.pop(0)
    return str(copy)