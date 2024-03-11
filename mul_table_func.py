"""
 Author: Elian
 Purpose: Contains a multiply function.
 Date: 11.03.2024
"""


def mul_table(num: int) -> list:
    """
    Return a list of the multiplied number.
    :param num: The number to multiply.
    :return: List of multiplied number.
    """
    return [num * i for i in range(1, num + 1)]
