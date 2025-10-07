import math
from pprint import pprint


def unsharp_mask(dim: int):
    """
    Creates an unsharp mask represented in a list from a specified dimension

    :param dim: int: unsharp mask dimensions (dim x dim)
    :return: list: A 2-dimensional unsharp mask
    """
    center = dim // 2
    return_list = [
        [value(x - center, y - center) for x in range(dim)]
        for y in range(dim)
    ]
    return return_list


def value(x, y):
    """
    Calculates value for point (x,y) according to negative gaussian blur formula

    :param x: int: x-value used in negative gaussian blur formula
    :param y: int: y-value used in negative gaussian blur formula
    :return: int: value calculated from negative gaussian blur formula
    """
    if x == 0 and y == 0:
        return 1.5
    s = 4.5
    ret = (-1 / (2 * math.pi * s ** 2)) * math.e ** (-((x ** 2 + y ** 2) / (2 * s ** 2)))
    return ret

# Test
if __name__ == "__main__":
    from pprint import pprint
    pprint(unsharp_mask(3))

