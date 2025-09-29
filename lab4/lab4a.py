"""
Different ways of splitting a string into one piece
    Containing lowercase, underscores and dots
    and another piece containing uppercase, spaces and pipes.
"""
from numpy._core.strings import islower
from numpy._core.strings import isupper

def split_rec(string: str, split1="", split2="") -> tuple[str, str]:
    """
    A recursive way of splitting a string into one piece
    Containing lowercase, underscores and dots
    and another piece containing uppercase, spaces and pipes.
    """
    current = string[0]

    if isupper(current) or current == " " or current == "|":
        split1 = str(split1 + current)

    elif islower(current) or current == "_" or current == ".":
        split2 = str(split2 + current)

    if len(string) - 1 <= 0:
        return split1, split2
    return split_rec(string[1 - len(string):], split1, split2)

def split_it(string):
    """
    An iterative way of splitting a string into one piece
    Containing lowercase, underscores and dots
    And another piece containing uppercase, spaces and pipes.
    """
    split1 = ""
    split2 = ""
    for i in string:
        if isupper(i) or i == " " or i == "|":
            split1 = str(split1 + i)

        elif islower(i) or i == "_" or i == ".":
            split2 = str(split2 + i)
    return split1, split2
