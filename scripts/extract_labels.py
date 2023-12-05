from tools.label_extract import extract_and_save_cvat_annotations
from defs.storage_locs import *

video_name = 'center_left_3_sunglare'
start_frame = 0
end_frame = 1000

extract_and_save_cvat_annotations(raw_annotations_path(video_name), PROCESSED_ANNOTATIONS_PATH, start_frame, end_frame)