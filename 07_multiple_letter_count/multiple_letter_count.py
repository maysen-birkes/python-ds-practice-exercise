def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    return {ltr: phrase.count(ltr) for ltr in phrase}

print(multiple_letter_count('yay'))
print(multiple_letter_count('Yay'))