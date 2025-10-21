import cv2
from lab5.cvlib import rgblist_to_cvimg
from lab5.lab5a1 import cvimg_to_list
from lab5.lab5b2 import generator_from_image


def gradient_condition(pixel):
    """
    Computes a normalized brightness value for a given pixel.

    """

    # Check that pixel has 3 color values and that pixel is a tuple
    if len(pixel) != 3:
        raise IndexError("Pixel must contain 3 numbers")
    if not isinstance(pixel, tuple):
        raise IndexError("Pixel must be a tuple")

    #Checks the that the values within pixel are color values
    for colors in pixel:
        if not isinstance(colors, int):
            raise TypeError("All HSV parameters must be integers")
        if colors < 0 or colors > 255:
            raise ValueError("All HSV parameters must be between 0 and 255")

    return (pixel[0]+pixel[1]+pixel[2]) / (255.0*3)




def combine_images(
        condition_list, gradient_condition, generator1, generator2):
    """
    Blends 2 images with the help of a third blend mask image.

    """
    result = []
    for i, pixel in enumerate(condition_list):
        try:
            condition_val = gradient_condition(pixel)
        except (IndexError, ValueError, TypeError):
            raise ValueError("Error in gradient_condition for value", pixel)

        try:
            pixel1 = generator1(i)
        except IndexError:
            raise ValueError(
                "Error in combine_images: generator1 raised IndexError")

        try:
            pixel2 = generator2(i)
        except IndexError:
            raise ValueError(
                "Error in combine_images: generator2 raised IndexError")

        # Calculate blended pixel
        blended_pixel = [
            int(pixel1[0] * condition_val + pixel2[0] * (1 - condition_val)),
            int(pixel1[1] * condition_val + pixel2[1] * (1 - condition_val)),
            int(pixel1[2] * condition_val + pixel2[2] * (1 - condition_val))
        ]
        result.append(blended_pixel)

    return result


if __name__ == "__main__":
    # Ladda bilderna
    img1 = cv2.imread("plane.jpg")  # Första bilden - generator1
    img2 = cv2.imread("gradient.jpg")  # Andra bilden - generator2
    mask_img = cv2.imread("image.png")  # Mask-bilden för övergången

    # Ser till att alla bilder har samma storlek
    target_shape = img1.shape
    if img2.shape != target_shape:
        img2 = cv2.resize(img2, (target_shape[1], target_shape[0]))
    if mask_img.shape != target_shape:
        mask_img = cv2.resize(mask_img, (target_shape[1], target_shape[0]))

    # Konverterar bilder till listor
    mask_list = cvimg_to_list(mask_img)
    img1_list = cvimg_to_list(img1)
    img2_list = cvimg_to_list(img2)

    # Skapa generatorer
    generator1 = generator_from_image(img1_list)
    generator2 = generator_from_image(img2_list)

    # Kombinera bilderna
    result = combine_images(
        mask_list, gradient_condition, generator1, generator2)

    # Visa resultatet
    new_img = rgblist_to_cvimg(result, img1.shape[0], img1.shape[1])
    cv2.imshow('Kombinerad bild', new_img)
    cv2.waitKey(0)