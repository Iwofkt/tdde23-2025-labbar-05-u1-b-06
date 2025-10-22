import cv2
from typing import List, Tuple, Callable
from cvlib import rgblist_to_cvimg
from lab5b1 import cvimg_to_list


def generator_from_image(
    image_list: List[Tuple[int, int, int]]
) -> Callable[[int], Tuple[int, int, int]]:
    """
    Create a generator function that returns pixel colors from an
    image.

    :param image_list: List of BGR pixel values from an image
    :return: Function that takes an index and returns corresponding
             pixel
    :raises IndexError: If index is out of bounds
    """
    def get_pixel(index: int) -> Tuple[int, int, int]:
        """
        Return the pixel at the given index from the image list.

        :param index: The index of the pixel to retrieve
        :return: The pixel value at the given index
        :raises IndexError: If index is out of bounds
        """
        if index < 0 or index >= len(image_list):
            raise IndexError(
                f"Index {index} is out of bounds for image list of length "
                f"{len(image_list)}"
            )
        return image_list[index]

    return get_pixel

# Test
if __name__ == "__main__":
    """
    Test function for generator_from_image by loading an image,
    creating a generator, and displaying both original and
    reconstructed images.
    """
    orig_img = cv2.imread("image.png")
    orig_list = cvimg_to_list(orig_img)

    generator = generator_from_image(orig_list)

    new_list = [generator(i) for i in range(len(orig_list))]

    cv2.imshow('original', orig_img)
    cv2.imshow(
        'new',
        rgblist_to_cvimg(
            new_list,
            orig_img.shape[0],
            orig_img.shape[1]
        )
    )
    cv2.waitKey(0)