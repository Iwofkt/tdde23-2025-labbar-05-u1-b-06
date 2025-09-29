import cv2

def cvimg_to_list (image):
    """
    :param image: cv2 object: cv3 information instance of an image
    :return: list: List of BGR vales for each pixel
    """
    return_list = []

    # Get the dimensions of the image
    height, width = image.shape[:2]

    for y in range(width):
        for x in range(height):
            return_list.append(image[x,y]) #BGR
    return return_list

#Test
#image = cv2.imread("image.png")
#cvimg_to_list(image)