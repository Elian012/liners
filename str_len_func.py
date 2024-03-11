"""
 Author: Elian
 Purpose: One line functions.
 Date: 11.03.2024
"""


def str_len(lst: list) -> list:
    """
    Returns a list with the len of each string.
    :param lst: List of strings.
    :return: New list of the lens.
    """
    return [len(word) for word in lst]
