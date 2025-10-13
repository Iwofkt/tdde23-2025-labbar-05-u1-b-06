def split_rec(string: str) -> tuple[str, str]:
    """
        Recursively split a string into two parts:
        One with lowercase letters, underscores, and dots
        One with uppercase letters, spaces, and pipes

        :param string: str: The input string to be split.
        :return: tuple[str, str]:
        First element contains lowercase letters, underscores, and dots.
        Second element contains uppercase letters, spaces, and pipes.
        """
    if not string:
        return "", ""

    current = string[0]
    lower_rest, upper_rest = split_rec(string[1:])

    if current.islower() or current in {"_", "."}:
        return current + lower_rest, upper_rest
    elif current.isupper() or current in {" ", "|"}:
        return lower_rest, current + upper_rest
    else:
        return lower_rest, upper_rest



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