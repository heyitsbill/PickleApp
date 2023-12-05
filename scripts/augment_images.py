from tools.data_loading import read_data_to_numpy, numpy_to_images_labels
from defs.storage_locs import VALID_DATASETS, VALID_FLIPPED_DATASETS
from tools.augment_images import apply_flip, apply_random_affine

# flip images
# for dataset in VALID_DATASETS:
#     X, y = read_data_to_numpy(dataset)
#     X, y = apply_flip(X, y)
#     numpy_to_images_labels(X, y, dataset + '_flip')

# # apply random affine
for dataset in VALID_DATASETS:
    X, y = read_data_to_numpy(dataset)
    X, y = apply_random_affine(X, y, 2, (-20, 20), ((-50, 50), (-25, 25)), replace_with='self')
    numpy_to_images_labels(X, y, dataset + '_affine')

for dataset in VALID_FLIPPED_DATASETS:
    X, y = read_data_to_numpy(dataset, custom=True)
    X, y = apply_random_affine(X, y, 2, (-20, 20), ((-50, 50), (-25, 25)), replace_with='self')
    numpy_to_images_labels(X, y, dataset + '_affine')
