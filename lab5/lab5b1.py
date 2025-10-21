import cv2
from cvlib import greyscale_list_to_cvimg
from lab5a1 import cvimg_to_list


def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """
    Creates a pixel constraint function for HSV color filtering.

    This function returns a callable that checks whether a pixel's HSV
    values
    fall within the specified ranges.

    :param hlow: int - Lower bound for hue.
    :param hhigh: int - Upper bound for hue.
    :param slow: int - Lower bound for saturation.
    :param shigh: int - Upper bound for saturation.
    :param vlow: int - Lower bound for value/brightness.
    :param vhigh: int - Upper bound for value/brightness.
    :return: function - A function that takes a pixel (h, s, v) tuple
    and returns 1 if the pixel is within range, else 0.
    :raises: ValueError if parameters are not in valid HSV range
    """
    # Validate that all parameters are within valid HSV range (0-255)
    parameters = [hlow, hhigh, slow, shigh, vlow, vhigh]
    for param in parameters:
        if not isinstance(param, int):
            raise ValueError("All HSV parameters must be integers")
        if param < 0 or param > 255:
            raise ValueError("All HSV parameters must be between 0 and 255")

    def is_black(pixel):
        """
        Determines if a given HSV pixel is within the predefined HSV
        constraints.

        :param pixel: tuple - A 3-tuple of integers (h, s, v)
        :return: int - 1 if pixel within range, else 0
        :raises: ValueError if pixel is not a valid 3-tuple
        """

        # Check that pixel has 3 color values and that pixel is a tuple
        if len(pixel) != 3:
            raise ValueError("Pixel must contain 3 numbers")
        if not isinstance(pixel, tuple):
            raise TypeError("Pixel must be a tuple")

        # Checks the that the values within pixel are color values
        for colors in pixel:
            if not isinstance(colors, int):
                raise TypeError("All HSV parameters must be integers")
            if colors < 0 or colors > 255:
                raise ValueError("All HSV parameters must be between 0 and 255")

        h, s, v = pixel
        return int(
            hlow < h < hhigh and slow < s < shigh and vlow < v < vhigh)

    return is_black


# test
if __name__ == "__main__":
    hsv_plane = cv2.cvtColor(cv2.imread("image.png"), cv2.COLOR_BGR2HSV)
    plane_list = cvimg_to_list(hsv_plane)

    is_sky = pixel_constraint(10, 200, 50, 200, 100, 255)
    sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))

    cv2.imshow('sky',greyscale_list_to_cvimg(sky_pixels,
                                             hsv_plane.shape[0],
                                             hsv_plane.shape[1]))
    cv2.waitKey(0)