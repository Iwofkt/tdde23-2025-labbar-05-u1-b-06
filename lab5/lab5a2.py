import math
from pprint import pprint
from typing import List


def unsharp_mask(dimension: int) -> list[list[float]]:
    """
    Creates an unsharp mask represented as a 2D list.

    :param dimension: int: mask size (dimension x dimension)
    :return: list: A 2-dimensional unsharp mask
    """

    def calculate_gaussian_value(x: int, y: int)-> float:
        """
        Calculates Gaussian blur value using negative Gaussian
        formula.

        :param x: int: x-coordinate relative to center
        :param y: int: y-coordinate relative to center
        :return: float: value from negative Gaussian blur formula
        """

        if x == 0 and y == 0:
            return 1.5

        s: float = 4.5
        exp_numerator: int = x ** 2 + y ** 2
        exp_denominator: float = 2 * s ** 2
        denominator: float = 2 * math.pi * s ** 2

        # Return value from given expression with variables s, x, y
        return (
                -(1 / denominator) *
                math.e ** (-exp_numerator / exp_denominator)
        )

    center: int = dimension // 2

    # List of values for each coordinate according to formula
    mask: List[List[float]] = [
        [
            calculate_gaussian_value(x - center, y - center)
         for x in range(dimension)
        ]
        for y in range(dimension)
    ]

    return mask


# Test
if __name__ == "__main__":
    pprint(unsharp_mask(3))
