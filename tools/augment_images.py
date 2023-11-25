import numpy as np
from tools.label_extract import group_points_by_2
import cv2

def apply_random_affine(X, y, times = 1, rotation_range = (0,0), translation_range = ((0,0), (0, 0)), replace_with = 'self'):
    """
    times: the number of times to apply transformation to whole set
        return will return n*times entries
    replace_with: "noise" or "self"
    X has shape n * height * width * 3
    y has shape n * num_points*2
    rotation_range: in degrees
    translation_range: in pixels
    """
    X_new = []
    y_new = []
    for i in range(times):
        for j in range(len(X)):
            img = X[j]
            labels = y[j]
            # apply transformation
            angle = np.random.uniform(rotation_range[0], rotation_range[1])/180 * np.pi
            dx = np.random.uniform(translation_range[0][0], translation_range[0][1])
            dy = np.random.uniform(translation_range[1][0], translation_range[1][1])
            
            rows, cols = img.shape[:2]
            center_dx = (cols/2) * (1 - np.cos(angle)) + (rows/2) * np.sin(angle)
            center_dy = (rows/2) * (1 - np.cos(angle)) - (cols/2) * np.sin(angle)
            dx = dx + center_dx
            dy = dy + center_dy
            M = np.float32([[np.cos(angle),-np.sin(angle),dx],[np.sin(angle),np.cos(angle),dy]])
            img_transformed = cv2.warpAffine(img, M, (cols, rows))

            # fill in empty space
            white = np.ones((rows, cols, 3), dtype=np.uint8) * 1
            mask = 1 - cv2.warpAffine(white,M,(cols,rows))

            if replace_with == 'self':
                img_transformed = img_transformed + img * mask
            elif replace_with == 'noise':
                noise = mask * np.random.randint(0, 255, (rows, cols, 3))
                img_transformed = img_transformed + noise * mask
            
            X_new.append(img_transformed)

            # transform labels
            point_labels = group_points_by_2(labels)
            new_labels = []
            for pair in point_labels:
                l = np.array(pair)
                l = np.append(l, 1)
                l = M @ l.T
                l = l.tolist()
                new_labels = new_labels + l
            
            y_new.append(new_labels)
    return (np.array(X_new), np.array(y_new))

def apply_random_affine_and_flip(X, y, times = 1, rotation_range = (0,0), translation_range = ((0,0), (0, 0)), replace_with = 'self', flip_rate = 0.5):
    """
    Horizontal flip
    """
    X_new, y_new = apply_random_affine(X, y, times, rotation_range, translation_range, replace_with)
    X_flip = []
    y_flip = []
    for i in range(len(X_new)):
        X = X_new[i]
        y = y_new[i]
        flip = np.random.random() < flip_rate
        if flip:
            X = cv2.flip(X, 1)
        
        width = X.shape[1]
        point_labels = group_points_by_2(y)
        new_labels = []
        for pair in point_labels:
            if flip:
                new_labels.append(width - pair[0])
            else:
                new_labels.append(pair[0])
            new_labels.append(pair[1])
        X_flip.append(X)
        y_flip.append(np.array(new_labels))
    return (np.array(X_flip), np.array(y_flip))


            





