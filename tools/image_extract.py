import cv2

def extract_images(video_path, milliseconds: list[int], output_path, image_name):
    cap = cv2.VideoCapture(video_path)
    for ms in milliseconds:
        cap.set(cv2.CAP_PROP_POS_MSEC, ms)
        success, image = cap.read()
        if success:
            cv2.imwrite(f'{output_path}/{image_name}_{ms}.jpg', image)

def extract_image(video_path, milliseconds: int, output_path, image_name):
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_MSEC, milliseconds)
    success, image = cap.read()
    if success:
        cv2.imwrite(f'{output_path}/{image_name}_{milliseconds}.jpg', image)
