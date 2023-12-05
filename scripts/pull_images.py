from tools.image_extract import extract_images

image_path = 'full_footage/center_right_1.MOV'
output_path = 'testing'

extract_images(image_path, [1000, 2000, 3000, 4000, 5000], output_path, 'center_right')