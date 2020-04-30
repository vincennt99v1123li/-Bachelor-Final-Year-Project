import os
import sys
import numpy as np
import cv2

IMAGE_SIZE = 64


# resize_image
def resize_image(image, height=IMAGE_SIZE, width=IMAGE_SIZE):
    top, bottom, left, right = (0, 0, 0, 0)

    # get image size
    h, w, _ = image.shape

    # find longest side of the image
    longest_edge = max(h, w)

    # calculate how many pixel is needed in order to same as the longer side's pixel
    if h < longest_edge:
        dh = longest_edge - h
        top = dh // 2
        bottom = dh - top
    elif w < longest_edge:
        dw = longest_edge - w
        left = dw // 2
        right = dw - left
    else:
        pass


    BLACK = [0, 0, 0]


    constant = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=BLACK)

    # resize complete
    return cv2.resize(constant, (height, width))



images = []
labels = []


def read_path(path_name):
    for dir_item in os.listdir(path_name):

        full_path = os.path.abspath(os.path.join(path_name, dir_item))
        print(full_path)
        if os.path.isdir(full_path):
            read_path(full_path)
        else:
            if dir_item.endswith('.jpg') or dir_item.endswith('.png') or dir_item.endswith('.jpeg') or dir_item.endswith('.JPG'):
                image = cv2.imread(full_path)
                image = resize_image(image, IMAGE_SIZE, IMAGE_SIZE)


                #cv2.imwrite('1.jpg', image)

                images.append(image)
                labels.append(path_name)

    return images, labels



def load_dataset(path_name,person_id):
    images, labels = read_path(path_name)


    images = np.array(images)
    print(images.shape)

    #if label.endswith('vin2'):
        #print(Y)


    labels = np.array([0 if label.endswith(str(person_id)) else 1 for label in labels ])
    print(labels)
    print(len(labels ))

    #i=0
    #while i<len(labels):
        #print(labels[i])


    return images, labels


if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage:%s path_name\r\n" % (sys.argv[0]))
    else:
        images, labels = load_dataset("images/")