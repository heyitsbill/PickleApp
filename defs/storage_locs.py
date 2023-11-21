from pathlib import Path
import os

RAW_VIDEO_PATH = 'full_footage/'
BASE_PATH = Path(__file__).parent.parent.parent if __file__ else Path('.')

def path_wrapper(path):
    return (BASE_PATH / path).as_posix()

def raw_video_path(type, filename):
    """
    type: 'court' or 'game'
    filename: ex. 'center_right_1.MOV'
    """
    if not filename.endswith('.MOV'):
        filename = filename + '.MOV'
    path = Path(RAW_VIDEO_PATH) / type / filename
    return path_wrapper(path)


EXTRACTED_PATH = 'data/extracted/'

def extracted_path(video_name):
    """
    video_name: ex. 'center_right_1'
    Create path if doesn't exist
    """
    path = Path(EXTRACTED_PATH) / video_name
    os.makedirs(path, exist_ok=True)
    return path_wrapper(path)
    
def extracted_image_path(video_name, frame):
    """
    video_name: ex. 'center_right_1'
    frame: ex. 0
    """
    path = Path(EXTRACTED_PATH) / video_name / f'{video_name}_{frame}.jpg'
    return path_wrapper(path)

def extracted_label_path(video_name):
    """
    video_name: ex. 'center_right_1'
    """
    path = Path(EXTRACTED_PATH) / video_name / f'{video_name}.json'
    return path_wrapper(path)
                        
RAW_ANNOTATIONS_PATH = 'annotations/raw'
PROCESSED_ANNOTATIONS_PATH = 'annotations/processed'

def raw_annotations_path(filename):
    """
    filename: ex. 'center_right_1.xml'
    """
    if not filename.endswith('.xml'):
        filename = filename + '.xml'
    path = Path(RAW_ANNOTATIONS_PATH) / filename
    return path_wrapper(path)

def processed_annotations_path(filename):
    """
    filename: ex. 'center_right_1.json'
    """
    if not filename.endswith('.json'):
        filename = filename + '.json'
    path = Path(PROCESSED_ANNOTATIONS_PATH) / filename
    return path_wrapper(path)

