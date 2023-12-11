import matplotlib.pyplot as plt
import cv2

def plot_image(img, figsize=(10, 10), color_transform=False, show_axes=True):
    """
    Plot the image
    """
    plt.figure(figsize=figsize)
    if color_transform:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    else:
        plt.imshow(img)
    if not show_axes:
        plt.axis('off')
        plt.tight_layout()
    plt.show()