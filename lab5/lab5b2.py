import cv2
from cvlib import rgblist_to_cvimg
from lab5b1 import cvimg_to_list


def generator_from_image(image_list):
    """
    Creates a generator function that returns pixel colors from an image list by index.

    :param image_list: list: List of BGR pixel values from an image
    :return: function: Generator function that takes an index and returns the corresponding pixel color
    :raises: IndexError if index is out of bounds
    """

    def get_pixel(index):
        """
        Returns the pixel at the given index from the image list.

        :param index: int - The index of the pixel to retrieve
        :return: tuple - The pixel value at the given index
        :raises: IndexError if index is out of bounds
        """
        if index < 0 or index >= len(image_list):
            raise IndexError(f"Index {index} is out of bounds for image list of length {len(image_list)}")
        return image_list[index]

    return get_pixel


# test
if __name__ == "__main__":
    """
    Test function for generator_from_image by loading an image, creating a generator,
    and displaying both original and reconstructed images.
    """
    orig_img = cv2.imread("image.png")
    orig_list = cvimg_to_list(orig_img)

    generator = generator_from_image(orig_list)

    new_list = [generator(i) for i in range(len(orig_list))]

    cv2.imshow('original', orig_img)
    cv2.imshow('new', rgblist_to_cvimg(new_list, orig_img.shape[0], orig_img.shape[1]))
    cv2.waitKey(0)