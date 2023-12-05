from tools.data_loading import load_numpy_data
from defs.storage_locs import ALL_DATASETS_NAMES

load_numpy_data(ALL_DATASETS_NAMES, '480x270', save_train_split=0.2)