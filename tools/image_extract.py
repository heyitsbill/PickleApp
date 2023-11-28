import cv2
from tools.label_extract import read_extracted_labels
import json
import os
import numpy as np
import shutil
from defs.storage_locs import *

def extract_images_from_frames(video_path, frames: list[int], output_path, image_name):
    cap = cv2.VideoCapture(video_path)
    for frame in frames:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        success, image = cap.read()
        if success:
            cv2.imwrite(f'{output_path}/{image_name}_{frame}.jpg', image)

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
        cv2.imwrite(f'{output_path}/{image_name}_{milliseconds}ms.jpg', image)

def extract_labeled_images(label_path, video_path, output_path, image_name):
    labels = read_extracted_labels(label_path)
    labeled_frames = list([int(frame) for frame in labels['frames'].keys()])
    extract_images_from_frames(video_path, labeled_frames, output_path, image_name)
    shutil.copy(label_path, os.path.join(output_path, os.path.basename(label_path)))

def read_frames(video_path, frames, resize_to = None, swap_colors = True):
    cap = cv2.VideoCapture(video_path)
    images = []
    for frame in frames:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        success, image = cap.read()
        if success:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            if resize_to is not None:
                image = cv2.resize(image, resize_to, interpolation=cv2.INTER_AREA)
            images.append(image)
    return np.array(images)

def read_frame(video_path, frame, resize_to = None, swap_colors = True):
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
    success, image = cap.read()
    if success:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if resize_to is not None:
            image = cv2.resize(image, resize_to, interpolation=cv2.INTER_AREA)
        return image
    return None