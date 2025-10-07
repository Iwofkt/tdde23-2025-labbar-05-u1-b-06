import cv2
import random
from lab5.cvlib import rgblist_to_cvimg
from lab5.lab5a1 import cvimg_to_list
from lab5.lab5b1 import pixel_constraint
from lab5.lab5b2 import generator_from_image
from lab5.lab5b3 import combine_images


def gradient_condition(pixel):
    return pixel[1]/255

if __name__ == "__main__":
    """
    Test function that combines a plane image with a starry sky effect using HSV color filtering.
    """
    # Read an image
    plane_img = cv2.imread("plane.jpg")

    # Create a filter that identifies the sky
    condition = pixel_constraint(100, 150, 50, 200, 100, 255)

    # Convert the original image to a list of HSV colors
    hsv_list = cvimg_to_list(cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV))
    plane_img_list = cvimg_to_list(plane_img)

    # Create a generator that makes a starry sky
    def generator1(index):
        val = random.random() * 255 if random.random() > 0.99 else 0
        return val, val, val

    # Create a generator for the loaded image
    generator2 = generator_from_image(plane_img_list)

    # Combine the two images into one, using the sky filter as a mask
    result = combine_images(hsv_list, condition, generator1, generator2)

    # Convert the result to a real image and display it
    new_img = rgblist_to_cvimg(result, plane_img.shape[0], plane_img.shape[1])
    cv2.imshow('Final image', new_img)
    cv2.waitKey(0)