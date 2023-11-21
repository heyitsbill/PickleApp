import cv2

def plot_labels(img, labels, color=(0, 255, 0), copy=True, withLines=False):
    """
    Plot the 10 labels on the image
    color should be in BGR format
    """
    if copy:
        img = img.copy()
    
    # scale circle and text label sizes according to image size
    if img.shape[0] > 1000:
        circle_size = 10
        text_size = 2
    else:
        circle_size = 2
        text_size = 1

    for i, label in enumerate(labels):
        cv2.circle(img, (int(label[0]), int(label[1])), circle_size, color, -1)
        # annotate with number
        cv2.putText(img, str(i+1), (int(label[0]), int(label[1])), cv2.FONT_HERSHEY_SIMPLEX, text_size, (0, 0, 0), 2)
    if withLines:
        labels = list(labels)
        # connect 1 to 3, 3 to 6, 6 to 4, 4 to 1, 9 to 10, 2 to 5
        connections = [(0, 2), (2, 5), (5, 3), (3, 0), (8, 9), (1, 4)]
        for connection in connections:
            cv2.line(img, (int(labels[connection[0]][0]), int(labels[connection[0]][1])), (int(labels[connection[1]][0]), int(labels[connection[1]][1])), color, 2)
    return img

