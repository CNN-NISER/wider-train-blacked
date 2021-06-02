import os
import cv2
import math

def create_dict(gt_file):
    """
    Returns a dictionary with image names as keys
    and coordinates of bounding boxes as values.
    """
    with open(gt_file) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    gt_dict = dict()
    key = ''
    value = []

    for i in range(len(lines)):
        element = lines[i]

        if element[-3:] == 'jpg':
            key = element
            value = []
            gt_dict[key] = value

        else:
            value_string = element.split(' ')
            value_int = [int(num) for num in value_string[:4]]
            gt_dict[key].append(value_int)

    return gt_dict

def blackout(image, bbox, image_path):
    """
    Blackout the lower half of a face
    and rewrite the file.
    """
    [x, y, w, h] = bbox
    black = [0,0,0]

    x_prime = x + w
    y_middle = y + math.ceil(h/2)
    y_bottom = y + h
    image[y_middle:y_bottom, x:x_prime] = black

    cv2.imwrite(image_path, image)

gt_labels = create_dict('labels.txt')

base_dir = os.path.join('WIDER_train', 'images')

for folder_name in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder_name)

    for image_name in os.listdir(folder_path):

        key = folder_name + "/" + image_name
        list_of_faces = gt_labels[key]
        image_path = os.path.join(folder_path, image_name)
        image = cv2.imread(image_path)

        # Loop over all faces
        for face in list_of_faces:
            blackout(image, face, image_path)
