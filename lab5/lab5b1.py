import cv2
from typing import List, Tuple, Callable
from cvlib import greyscale_list_to_cvimg
from lab5a1 import cvimg_to_list


def pixel_constraint(
    hlow: int,
    hhigh: int,
    slow: int,
    shigh: int,
    vlow: int,
    vhigh: int
) -> Callable[[Tuple[int, int, int]], int]:
    """
    Create a pixel constraint function for HSV color filtering.

    Returns a callable that checks whether a pixel's HSV values
    fall within the specified ranges.

    :param hlow: Lower bound for hue
    :param hhigh: Upper bound for hue
    :param slow: Lower bound for saturation
    :param shigh: Upper bound for saturation
    :param vlow: Lower bound for value/brightness
    :param vhigh: Upper bound for value/brightness
    :return: Function that takes a pixel (h, s, v) tuple and returns
             1 if within range, else 0
    :raises ValueError: If parameters are not in valid HSV range
    """
    # Validate that all parameters are within valid HSV range (0-255)
    parameters: List[int] = [hlow, hhigh, slow, shigh, vlow, vhigh]
    for param in parameters:
        if not isinstance(param, int):
            raise ValueError("All HSV parameters must be integers")
        if param < 0 or param > 255:
            raise ValueError("All HSV parameters must be between 0 and 255")

    def is_black(pixel: Tuple[int, int, int]) -> int:
        """
        Determine if a given HSV pixel is within the predefined
        constraints.

        :param pixel: A 3-tuple of integers (h, s, v)
        :return: 1 if pixel within range, else 0
        :raises ValueError: If pixel is not a valid 3-tuple
        :raises TypeError: If pixel has incorrect types
        """
        # Check that pixel has 3 color values and that pixel is a tuple
        if not isinstance(pixel, tuple):
            raise TypeError("Pixel must be a tuple")
        if len(pixel) != 3:
            raise ValueError("Pixel must contain exactly 3 numbers")

        # Check that the values within pixel are valid color values
        for color in pixel:
            if not isinstance(color, int):
                raise TypeError("All HSV parameters must be integers")
            if color < 0 or color > 255:
                raise ValueError(
                    "All HSV parameters must be between 0 and 255"
                )

        h, s, v = pixel
        return int(
            hlow < h < hhigh and slow < s < shigh and vlow < v < vhigh
        )

    return is_black


# Test
if __name__ == "__main__":
    hsv_plane = cv2.cvtColor(cv2.imread("image.png"), cv2.COLOR_BGR2HSV)
    plane_list = cvimg_to_list(hsv_plane)

    is_sky = pixel_constraint(10, 200, 50, 200, 100, 255)
    sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))

    cv2.imshow(
        'sky',
        greyscale_list_to_cvimg(
            sky_pixels,
            hsv_plane.shape[0],
            hsv_plane.shape[1]
        )
    )
    cv2.waitKey(0)