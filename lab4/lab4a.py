def split_rec(string: str, split1: str = "", split2: str = "") -> tuple[str, str]:
    """
    Recursively split a string into two parts:
    One with uppercase letters, spaces, and pipes
    One with lowercase letters, underscores, and dots

    :param string: str: The input string to be split.
    :param split1: str: Accumulator for uppercase, spaces, and pipes (used during recursion).
    :param split2: str: Accumulator for lowercase, underscore, and dot characters (used during recursion).
    :return: tuple[str, str]: A tuple where:
    First element contains uppercase letters, spaces, and pipes.
    Second element contains lowercase letters, underscores, and dots.
    """
    current = string[0]

    if current.islower() or current in {"_", "."}:
        split1 += current
    elif current.isupper() or current in {" ", "|"}:
        split2 += current

    if len(string) == 1:
        return split1, split2
    return split_rec(string[1:], split1, split2)


def split_it(string: str) -> tuple[str, str]:
    """
    Iteratively split a string into two parts:
    One with uppercase letters, spaces, and pipes
    One with lowercase letters, underscores, and dots

    :param string: str: The input string to be split.
    :return: tuple[str, str]:
    First element contains uppercase letters, spaces, and pipes.
    Second element contains lowercase letters, underscores, and dots.
    """
    split1 = ""
    split2 = ""

    for char in string:
        if char.islower() or char in {"_", "."}:
            split1 += char
        elif char.isupper() or char in {" ", "|"}:
            split2 += char

    return split1 ,split2