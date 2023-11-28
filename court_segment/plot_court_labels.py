import cv2
import random
from tools.label_extract import group_points_by_2
from tools.visualization import plot_image
import numpy as np

def plot_labels(img, labels, color=(0, 255, 0), copy=True, withLines=False, withText=True, scale_labels=True):
    """
    Plot the 10 labels on the image
    color should be in BGR format
    """
    if copy:
        img = img.copy().astype('uint8')

    if scale_labels and isinstance(labels, np.ndarray):
        label_dimensions = (1920, 1080)
        scaling_factor = (img.shape[1]/label_dimensions[0], img.shape[0]/label_dimensions[1])
        num_coords = labels.size
        labels = labels.reshape(-1, num_coords//2, 2)
        labels = labels * scaling_factor
        labels = labels.reshape(num_coords)

    if not isinstance(labels, list):
        labels = group_points_by_2(labels)
    
    # scale circle and text label sizes according to image size
    if img.shape[0] > 1000:
        circle_size = 10
        text_size = 2
    else:
        circle_size = 2
        text_size = 0.5

    for i, label in enumerate(labels):
        cv2.circle(img, (int(label[0]), int(label[1])), circle_size, color, -1)
        # annotate with number
        if withText:
            cv2.putText(img, str(i+1), (int(label[0]), int(label[1])), cv2.FONT_HERSHEY_SIMPLEX, text_size, (0, 0, 0), text_size)
    if withLines:
        labels = list(labels)
        # connect 1 to 3, 3 to 6, 6 to 4, 4 to 1, 9 to 10, 2 to 5
        connections = [(0, 2), (2, 5), (5, 3), (3, 0), (8, 9), (1, 4)]
        connections = [c for c in connections if c[0]<len(labels) and c[1]<len(labels)]
        for connection in connections:
            cv2.line(img, (int(labels[connection[0]][0]), int(labels[connection[0]][1])), (int(labels[connection[1]][0]), int(labels[connection[1]][1])), color, 2)
    return img

def plot_random_labeled_image(X, y, withLines = False, scale_labels = True):
    """
    If scale_labels is True, then the labels are scaled to the image size
    """
    if scale_labels:
        label_dimensions = (1920, 1080)
        scaling_factor = (X.shape[2]/label_dimensions[0], X.shape[1]/label_dimensions[1])
        num_coords = y.shape[1]
        y = y.reshape(-1, num_coords//2, 2)
        y = y * scaling_factor
        y = y.reshape(-1, num_coords)

    sample = random.randint(0, len(X)-1)
    img = X[sample]
    labels = y[sample]
    labels = group_points_by_2(labels)
    plotted = plot_labels(img, labels, withLines=withLines)
    plot_image(plotted)
    pass
