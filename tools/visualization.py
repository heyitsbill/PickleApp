import matplotlib.pyplot as plt
import cv2

def plot_image(img, figsize=(10, 10), color_transform=False):
    """
    Plot the image
    """
    plt.figure(figsize=figsize)
    if color_transform:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    else:
        plt.imshow(img)
    plt.show()