import cv2
from cvlib import rgblist_to_cvimg


def cvimg_to_list(image):
    """
    Creates a list of the BGR values for each pixel in an image.

    :param image: numpy array: image to interpret
    :return: list: List of BGR vales for each pixel
    """
    return [tuple(map(int, pixel)) for row in image for pixel in row]


# Test
if __name__ == "__main__":
    test_file = "image.png"
    test_image = cv2.imread(test_file)

    if test_image is None:
        raise FileNotFoundError(f"Could not read image file: {test_file}")

    bgr_test_list = cvimg_to_list(test_image)
    print(bgr_test_list)

    test_height, test_width = test_image.shape[:2]
    cv2.imshow("test", rgblist_to_cvimg(bgr_test_list, test_height, test_width))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
