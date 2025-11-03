import cv2
import numpy as np
from typing import List, Tuple, Callable
from lab5.cvlib import rgblist_to_cvimg
from lab5.lab5a1 import cvimg_to_list
from lab5.lab5b2 import generator_from_image


def gradient_condition(pixel: Tuple[int, int, int]) -> float:
    """
    Compute a normalized brightness value for a given pixel.

    :param pixel: A 3-tuple of integers representing RGB values
    :return: Normalized brightness value between 0.0 and 1.0
    :raises IndexError: If pixel is not a 3-element tuple
    :raises TypeError: If pixel contains non-integer values
    :raises ValueError: If pixel values are outside 0-255 range
    """
    # Check that pixel has 3 color values and that pixel is a tuple
    if not isinstance(pixel, tuple):
        raise IndexError("Pixel must be a tuple")
    if len(pixel) != 3:
        raise IndexError("Pixel must contain exactly 3 numbers")

    # Check that the values within pixel are valid color values
    for color in pixel:
        if not isinstance(color, int):
            raise TypeError("All color parameters must be integers")
        if color < 0 or color > 255:
            raise ValueError("All color parameters must be between 0 and 255")

    return (pixel[0] + pixel[1] + pixel[2]) / (255.0 * 3)


def combine_images(
    condition_list: List[Tuple[int, int, int]],
    gradient_condition: Callable[[Tuple[int, int, int]], float],
    generator1: Callable[[int], Tuple[int, int, int]],
    generator2: Callable[[int], Tuple[int, int, int]]
) -> List[Tuple[int, int, int]]:
    """
    Blend 2 images with the help of a third blend mask image.

    :param condition_list: List of pixels used for blending weights
    :param gradient_condition: Function that computes blend weight from pixel
    :param generator1: Function providing pixels from first image
    :param generator2: Function providing pixels from second image
    :return: List of blended RGB pixel values
    :raises ValueError: If any generator raises IndexError
    """
    result: List[Tuple[int, int, int]] = []
    for i, pixel in enumerate(condition_list):
        try:
            condition_val: float = gradient_condition(pixel)
        except (IndexError, ValueError, TypeError):
            raise ValueError(f"Error in gradient_condition for value {pixel}")

        try:
            pixel1: Tuple[int, int, int] = generator1(i)
        except IndexError:
            raise ValueError(
                "Error in combine_images: generator1 raised IndexError"
            )

        try:
            pixel2: Tuple[int, int, int] = generator2(i)
        except IndexError:
            raise ValueError(
                "Error in combine_images: generator2 raised IndexError"
            )

        # Calculate blended pixel
        blended_pixel: Tuple[int, int, int] = (
            int(pixel1[0] * condition_val + pixel2[0] * (1 - condition_val)),
            int(pixel1[1] * condition_val + pixel2[1] * (1 - condition_val)),
            int(pixel1[2] * condition_val + pixel2[2] * (1 - condition_val))
        )
        result.append(blended_pixel)

    return result


if __name__ == "__main__":
    # Load images

    # First image - generator1
    img1: np.ndarray = cv2.imread("plane.jpg")
    # Second image - generator2
    img2: np.ndarray = cv2.imread("gradient.jpg")
    # Mask image for transition
    mask_img: np.ndarray = cv2.imread("image.png")

    # Ensure all images have the same size
    target_shape: Tuple[int, ...] = img1.shape
    if img2.shape != target_shape:
        img2 = cv2.resize(img2, (target_shape[1], target_shape[0]))
    if mask_img.shape != target_shape:
        mask_img = cv2.resize(mask_img, (target_shape[1], target_shape[0]))

    # Convert images to lists
    mask_list: List[Tuple[int, int, int]] = cvimg_to_list(mask_img)
    img1_list: List[Tuple[int, int, int]] = cvimg_to_list(img1)
    img2_list: List[Tuple[int, int, int]] = cvimg_to_list(img2)

    # Create generators
    generator1: Callable[[int], Tuple[int, int, int]] = generator_from_image(
        img1_list
    )
    generator2: Callable[[int], Tuple[int, int, int]] = generator_from_image(
        img2_list
    )

    # Combine images
    result: List[Tuple[int, int, int]] = combine_images(
        mask_list, gradient_condition, generator1, generator2
    )

    # Display result
    new_img: np.ndarray = rgblist_to_cvimg(
        result, img1.shape[0], img1.shape[1]
    )
    cv2.imshow('Combined image', new_img)
    cv2.waitKey(0)
