def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    revstring = value[::-1]
    if value.replace(" ", "").lower() == revstring.replace(" ", "").lower():
        return True
    else:
        return False

