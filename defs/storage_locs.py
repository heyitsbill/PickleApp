from pathlib import Path
import os

RAW_VIDEO_PATH = 'full_footage/'

def raw_video_path(type, filename):
    """
    type: 'court' or 'game'
    filename: ex. 'center_right_1.MOV'
    """
    if not filename.endswith('.MOV'):
        filename = filename + '.MOV'
    path = Path(RAW_VIDEO_PATH) / type / filename
    return path.as_posix()


EXTRACTED_PATH = 'data/extracted/'

def extracted_path(video_name):
    """
    video_name: ex. 'center_right_1'
    Create path if doesn't exist
    """
    path = Path(EXTRACTED_PATH) / video_name
    os.makedirs(path, exist_ok=True)
    return path.as_posix()
    
RAW_ANNOTATIONS_PATH = 'annotations/raw'
PROCESSED_ANNOTATIONS_PATH = 'annotations/processed'

def raw_annotations_path(filename):
    """
    filename: ex. 'center_right_1.xml'
    """
    if not filename.endswith('.xml'):
        filename = filename + '.xml'
    path = Path(RAW_ANNOTATIONS_PATH) / filename
    return path.as_posix()

def processed_annotations_path(filename):
    """
    filename: ex. 'center_right_1.json'
    """
    if not filename.endswith('.json'):
        filename = filename + '.json'
    path = Path(PROCESSED_ANNOTATIONS_PATH) / filename
    return path.as_posix()