import cv2
import random
import numpy as np
from typing import List, Tuple, Callable
from lab5.cvlib import rgblist_to_cvimg
from lab5.lab5a1 import cvimg_to_list
from lab5.lab5b1 import pixel_constraint
from lab5.lab5b2 import generator_from_image


def combine_images(
    hsv_img_list: List[Tuple[int, int, int]],
    condition: Callable[[Tuple[int, int, int]], bool],
    condition_img: Callable[[int], Tuple[int, int, int]],
    start_img: Callable[[int], Tuple[int, int, int]]
) -> List[Tuple[int, int, int]]:
    """
    Combine two images based on a condition.

    Uses pixels from one image where the condition is true
    and from the other image where the condition is false.

    :param hsv_img_list: List of HSV pixel values for condition
                         checking
    :param condition: Function that takes an HSV pixel and returns
                      bool
    :param condition_img: Function that provides pixels when condition
                          is True
    :param start_img: Function that provides pixels when condition is
                      False
    :return: Combined list of RGB pixel values
    """
    return [
        condition_img(i) if condition(hsv_pixel) else start_img(i)
        for i, hsv_pixel in enumerate(hsv_img_list)
    ]


if __name__ == "__main__":
    """
    Test function that combines a plane image with a starry sky
    effect using HSV color filtering.
    """
    # Read an image
    plane_img: np.ndarray = cv2.imread("plane.jpg")

    # Create a filter that identifies the sky
    condition: Callable[[Tuple[int, int, int]], int] = pixel_constraint(
        100, 150, 50, 200, 100, 255
    )

    # Convert the original image to a list of HSV colors
    hsv_list: List[Tuple[int, int, int]] = cvimg_to_list(
        cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV)
    )
    plane_img_list: List[Tuple[int, int, int]] = cvimg_to_list(plane_img)

    # Create a generator that makes a starry sky
    def generator1(index: int) -> Tuple[float, float, float]:
        val: float = random.random() * 255 if random.random() > 0.99 else 0
        return val, val, val

    # Create a generator for the loaded image
    generator2: Callable[[int], Tuple[int, int, int]] = generator_from_image(
        plane_img_list
    )

    # Combine the two images into one, using the sky filter as a mask
    result: List[Tuple[int, int, int]] = combine_images(
        hsv_list, condition, generator1, generator2
    )

    # Convert the result to a real image and display it
    new_img: np.ndarray = rgblist_to_cvimg(
        result,
        plane_img.shape[0],
        plane_img.shape[1]
    )
    cv2.imshow('Final image', new_img)
    cv2.waitKey(0)
