# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alpahbetical order.
#
# You can either enter the text from the keybord or
# Initialise a string variable with the string

def constanace_only(phrase: str) -> list:
    """
    Converts a `str` to list of non
    vowels in alphabetical order.

    :param phrase: The string entered by a user.
    :return: The alphabetically ordered list of non vowels
    """
    vowels = frozenset("aeiou")
    words = set(phrase).difference(vowels)

    return sorted(list(words))


x = input("Enter a phrase without any words: ")
print(constanace_only(x))