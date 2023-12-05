from defs.storage_locs import *
from tools.image_extract import *

# extract_labeled_images('testing/center_left_1.json', raw_video_path('court', 'center_left_1.MOV'), extracted_path('center_left_1'), 'center_left_1')
# extract_labeled_images(processed_annotations_path('center_right_1'), raw_video_path('court', 'center_right_1'), extracted_path('center_right_1'), 'center_right_1')
extract_labeled_images(processed_annotations_path('center_left_3_sunglare'), raw_video_path('court', 'center_left_3_sunglare'), extracted_path('center_left_3_sunglare'), 'center_left_3_sunglare')