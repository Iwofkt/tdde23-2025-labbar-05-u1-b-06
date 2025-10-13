import cv2
from lab5.cvlib import rgblist_to_cvimg
from lab5.lab5a1 import cvimg_to_list
from lab5.lab5b2 import generator_from_image


def gradient_condition(pixel):
    """
    Returnerar ett värde mellan 0 och 1 baserat på pixelens ljusstyrka.
    """
    return pixel[0] / 255.0


def combine_images(condition_list, condition_func, generator1, generator2):
    """
    Kombinerar två bilder med formeln: generator1 * condition + generator2 * (1 - condition)
    """
    return [
        [
            int(generator1(i)[0] * condition_func(pixel) + generator2(i)[0] * (1 - condition_func(pixel))),
            int(generator1(i)[1] * condition_func(pixel) + generator2(i)[1] * (1 - condition_func(pixel))),
            int(generator1(i)[2] * condition_func(pixel) + generator2(i)[2] * (1 - condition_func(pixel)))
        ]
        for i, pixel in enumerate(condition_list)
    ]


if __name__ == "__main__":
    # Ladda bilderna
    img1 = cv2.imread("plane.jpg")  # Första bilden - generator1
    img2 = cv2.imread("gradient.jpg")  # Andra bilden - generator2
    mask_img = cv2.imread("image.png")  # Mask-bilden för övergången

    # Se till att alla bilder har samma storlek
    target_shape = img1.shape
    if img2.shape != target_shape:
        img2 = cv2.resize(img2, (target_shape[1], target_shape[0]))
    if mask_img.shape != target_shape:
        mask_img = cv2.resize(mask_img, (target_shape[1], target_shape[0]))

    # Konvertera till listor
    mask_list = cvimg_to_list(mask_img)
    img1_list = cvimg_to_list(img1)
    img2_list = cvimg_to_list(img2)

    # Skapa generatorer
    generator1 = generator_from_image(img1_list)
    generator2 = generator_from_image(img2_list)

    # Kombinera bilderna
    result = combine_images(mask_list, gradient_condition, generator1, generator2)

    # Visa resultatet
    new_img = rgblist_to_cvimg(result, img1.shape[0], img1.shape[1])
    cv2.imshow('Kombinerad bild', new_img)
    cv2.waitKey(0)