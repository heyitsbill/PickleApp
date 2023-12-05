from tools.data_loading import save_data_to_numpy, load_numpy_data
from defs.storage_locs import VALID_DATASETS, VALID_CUSTOM_DATASETS
# for dataset in VALID_DATASETS:
#     save_data_to_numpy(dataset, resize_to = (480, 270))
# load_numpy_data(VALID_DATASETS, '480x270', save_train_split=0.2)
# save_data_to_numpy('test', resize_to = (480, 270), custom=True)

for dataset in VALID_DATASETS:
    save_data_to_numpy(dataset, resize_to = (480, 270))

for dataset in VALID_CUSTOM_DATASETS:
    save_data_to_numpy(dataset, resize_to = (480, 270), custom=True)