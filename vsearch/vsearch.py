def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    result = set(letters).intersection(set(phrase))

    if(bool(set(letters).intersection(set(phrase)))==True):     # Vowels were found
        return set(letters).intersection(set(phrase))
    elif(len(phrase)==0):       # Phrase was sent empty
        return "Phrase is Empty!"
    else:                     # No Vowels found
        return "No Vowels found in the Phrase"
