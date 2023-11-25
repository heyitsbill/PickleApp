from pathlib import Path
import os

VALID_DATASETS = ['center_left_1', 'center_right_1', 'center_left_3_sunglare']

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

NUMPY_DATA_PATH = 'data/numpy'

def numpy_data_filepaths(video_name, shape):
    """
    video_name: ex. 'center_right_1'
    shape: ex. '224x224' width x height
    returns [data/numpy/video_name_X.npy, data/numpy/video_name_y.npy]
    """
    path = Path(NUMPY_DATA_PATH) / shape
    os.makedirs(path, exist_ok=True)
    paths = [path / f'{video_name}_X.npy', path / f'{video_name}_y.npy']
    return [path_wrapper(path) for path in paths]

WEIGHTS_PATH = 'weights/'

def weights_file(filename):
    """
    filename: ex. 'center_right_1.h5'
    """
    if not filename.endswith('.h5'):
        filename = filename + '.h5'
    path = Path(WEIGHTS_PATH) / filename
    return path_wrapper(path)

CUSTOM_PATH = 'data/custom/'

def custom_path(data_name):
    path = Path(CUSTOM_PATH) / data_name
    os.makedirs(path, exist_ok=True)
    return path_wrapper(path)

def custom_image_path(data_name, frame):
    path = Path(CUSTOM_PATH) / data_name / f'{data_name}_{frame}.jpg'
    return path_wrapper(path)

def custom_label_path(data_name):
    path = Path(CUSTOM_PATH) / data_name / f'{data_name}.pkl'
    return path_wrapper(path)
