import cv2

def cvimg_to_list (file):
    """
    Finds the BGR values for each pixel in an image

    :param file: str: location of image to interpret
    :return: list: List of BGR vales for each pixel
    """
    image = cv2.imread(file)
    return_list = []

    # Get the dimensions of the image
    height, width = image.shape[:2]

    return_list = [
        [image[row,column] for column in range(width)]
        for row in range(height)
    ]
    return return_list

#Test
#print(cvimg_to_list("image.png"))