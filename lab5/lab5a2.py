import math
from pprint import pprint


def unsharp_mask(dimension: int):
    """
    Creates an unsharp mask represented as a 2D list.

    :param dimension: int: mask size (dimension x dimension)
    :return: list: A 2-dimensional unsharp mask
    """

    def calculate_gaussian_value(x: int, y: int):
        """
        Calculates Gaussian blur value using negative Gaussian formula.

        :param x: int: x-coordinate relative to center
        :param y: int: y-coordinate relative to center
        :return: float: value from negative Gaussian blur formula
        """

        if x == 0 and y == 0:
            return 1.5

        s = 4.5
        exp_numerator = x ** 2 + y ** 2
        exp_denominator = 2 * s ** 2
        denominator = 2 * math.pi * s ** 2

        # Return value from given expression with variables s, x, y
        return (-(1 / denominator) *
                math.e ** (-exp_numerator / exp_denominator))

    center = dimension // 2

    # List of values for each coordinate according to formula
    mask = [
        [calculate_gaussian_value(x - center, y - center)
         for x in range(dimension)]
        for y in range(dimension)
    ]

    return mask


# Test
if __name__ == "__main__":
    pprint(unsharp_mask(3))