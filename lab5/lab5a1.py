import cv2
import numpy as np
from typing import List, Tuple
from cvlib import rgblist_to_cvimg


def cvimg_to_list(image: np.ndarray) -> List[Tuple[int, int, int]]:
    """
    Create a list of tuples with the BGR values for each pixel in an
    image.

    :param image: numpy array representing the image to interpret
    :return: list of BGR values for each pixel in the image
    """
    return [tuple(map(int, pixel)) for row in image for pixel in row]


# Test
if __name__ == "__main__":
    test_file: str = "image.png"
    test_image: np.ndarray = cv2.imread(test_file)

    if test_image is None:
        raise FileNotFoundError(f"Could not read image file: {test_file}")

    bgr_test_list: List[Tuple[int, int, int]] = cvimg_to_list(test_image)
    print(bgr_test_list)

    test_height, test_width = test_image.shape[:2]
    cv2.imshow(
        "test",
        rgblist_to_cvimg(bgr_test_list, test_height, test_width)
    )

    cv2.waitKey(0)
    cv2.destroyAllWindows()