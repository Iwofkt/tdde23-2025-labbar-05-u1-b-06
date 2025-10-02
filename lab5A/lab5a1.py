import cv2
from cvlib import rgblist_to_cvimg

def cvimg_to_list (file):
    """
    Creates a list of the BGR values for each pixel in an image

    :param file: str: location of image to interpret
    :return: list: List of BGR vales for each pixel
    """
    image = cv2.imread(file)

    bgr_list = [tuple(map(int, pixel)) for row in image for pixel in row]

    return bgr_list

#Test
"""test_file = "image.png"

bgr_test_list = cvimg_to_list(test_file)
print(bgr_test_list)

test_image = cv2.imread(test_file)

test_height, test_width = test_image.shape[:2]
cv2.imshow("test", rgblist_to_cvimg(bgr_test_list, int(test_height), int(test_width)))

cv2.waitKey(0)"""