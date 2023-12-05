from tools.data_loading import read_data_to_numpy, numpy_to_images_labels, \
                               save_data_to_numpy, load_numpy_data
from defs.storage_locs import VALID_DATASETS
from sklearn.model_selection import train_test_split
from tools.augment_images import apply_flip, apply_random_affine

# print(VALID_DATASETS)
# for dataset in VALID_DATASETS:
#     X, y = read_data_to_numpy(dataset)
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#     numpy_to_images_labels(X_train, y_train, dataset + '_train')
#     numpy_to_images_labels(X_test, y_test, dataset + '_test')

custom_datasets = [d + '_train' for d in VALID_DATASETS] + [d + '_test' for d in VALID_DATASETS]

# print(custom_datasets)
# # apply flips
# for dataset in custom_datasets:
#     X, y = read_data_to_numpy(dataset, custom=True)
#     X, y = apply_flip(X, y)
#     numpy_to_images_labels(X, y, dataset + '_flip')

custom_datasets = [d + '_flip' for d in custom_datasets] + custom_datasets

# print(custom_datasets)
# # apply random affine
# for dataset in custom_datasets:
#     X, y = read_data_to_numpy(dataset, custom=True)
#     X, y = apply_random_affine(X, y, 2, (-20, 20), ((-50, 50), (-25, 25)), replace_with='self')
#     numpy_to_images_labels(X, y, dataset + '_affine')

custom_datasets = [d + '_affine' for d in custom_datasets] + custom_datasets

print(custom_datasets)
# save to numpy
size = (224, 224)
for data in custom_datasets:
    save_data_to_numpy(data, resize_to = size, custom=True)

test_datasets = [d for d in custom_datasets if '_test' in d]
train_datasets = [d for d in custom_datasets if '_train' in d]
original_tests = [d for d in test_datasets if '_affine' not in d]
original_trains = [d for d in train_datasets if '_affine' not in d]
right_orient_train_datasets = [d for d in train_datasets if ('right' in d and 'flip' not in d) or ('left' in d and 'flip' in d)]
right_orient_test_datasets = [d for d in test_datasets if ('right' in d and 'flip' not in d) or ('left' in d and 'flip' in d)]

# load numpy data
size = '224x224'
dirname = '224x224_sized'
load_numpy_data(original_tests, size, save=True, save_name='noaug_test', output_dirname=dirname)
load_numpy_data(original_trains, size, save=True, save_name='noaug_train', output_dirname=dirname)
load_numpy_data(test_datasets, size, save=True, save_name='test', output_dirname=dirname)
load_numpy_data(train_datasets, size, save=True, save_name='train', output_dirname=dirname)
load_numpy_data(right_orient_train_datasets, size, save=True, save_name='right_orient_train', output_dirname=dirname)
load_numpy_data(right_orient_test_datasets, size, save=True, save_name='right_orient_test', output_dirname=dirname)