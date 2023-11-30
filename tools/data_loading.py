from defs.storage_locs import *
from tools.label_extract import read_extracted_labels, labels_to_simple_df
import cv2
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle

POINT_LABELS = ['1_x', '1_y', '2_x', '2_y', '3_x', '3_y', '4_x', '4_y',
                '5_x', '5_y', '6_x', '6_y', '7_x', '7_y', '8_x', '8_y',
                '9_x', '9_y', '10_x', '10_y']

def read_data_to_numpy(dataset_name, resize_to = None, custom = False):
    X = []
    y = []
    if not custom:
        labels = labels_to_simple_df(read_extracted_labels(extracted_label_path(dataset_name)))
    else:
        labels = pd.read_json(custom_label_path(dataset_name), orient='records')

    for index, row in labels.iterrows():
        frame = int(row['frame_num'])
        if not custom:
            img = cv2.imread(extracted_image_path(dataset_name, frame))
        else:
            img = cv2.imread(custom_image_path(dataset_name, frame))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if resize_to is not None:
            img = cv2.resize(img, resize_to, interpolation=cv2.INTER_AREA)
        X.append(img)
    y.append(labels[POINT_LABELS].reset_index(drop=True))
    X = np.array(X)
    y = np.array(pd.concat(y)).astype('float32')
    return (X, y)

def save_data_to_numpy(dataset_name, resize_to = None, outx_path = None, outy_path = None, custom=False):
    """
    resize_to: (width, height)
    """
    # X = []
    # y = []
    # labels = labels_to_simple_df(read_extracted_labels(extracted_label_path(dataset_name)))
    # for index, row in labels.iterrows():
    #     frame = row['frame_num']
    #     img = cv2.imread(extracted_image_path(dataset_name, frame))
    #     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #     if resize_to is not None:
    #         img = cv2.resize(img, resize_to, interpolation=cv2.INTER_AREA)
    #     X.append(img)
    # y.append(labels[POINT_LABELS].reset_index(drop=True))
    # X = np.array(X)
    # y = np.array(pd.concat(y)).astype('float32')
    X, y = read_data_to_numpy(dataset_name, resize_to, custom)
    height_width = X[0].shape[:2]
    shape = f'{height_width[1]}x{height_width[0]}'
    default_outx_path = numpy_data_filepaths(dataset_name, shape)[0]
    default_outy_path = numpy_data_filepaths(dataset_name, shape)[1]
    print("Saving data with shape (width, height):", shape, "for dataset", dataset_name, f"({len(X)} images)")
    if outx_path is not None:
        np.save(outx_path, X)
    else:
        np.save(default_outx_path, X)
    if outy_path is not None:
        np.save(outy_path, y)
    else:
        np.save(default_outy_path, y)
    return X, y

def load_numpy_data(dataset_names, shape, save = True, save_train_split = None, save_name=None, input_dirname = None, output_dirname = None):
    """
    shape: string with format 'widthxheight'
    return X and y as numpy arrays with all the data
    save_train_split: ratio of data to save for testing
    """
    if save_name is None:
        save_name = 'all'
    
    if isinstance(dataset_names, str):
        dataset_names = [dataset_names]
    X = []
    y = []
    for dataset_name in dataset_names:
        X.append(np.load(numpy_data_filepaths(dataset_name, shape, input_dirname)[0]))#, allow_pickle=True))
        y.append(np.load(numpy_data_filepaths(dataset_name, shape, input_dirname)[1], allow_pickle=True))
    X = np.concatenate(X, axis=0)
    y = np.concatenate(y, axis=0)
    if save:
        np.save(numpy_data_filepaths(save_name, shape, output_dirname)[0], X)
        np.save(numpy_data_filepaths(save_name, shape, output_dirname)[1], y)
        print("Saved data with shape (width, height):", shape, f"for {len(dataset_names)} datasets", dataset_names, f"({len(X)} images total)")
    
    if (save_train_split is not None) and save:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=save_train_split, random_state=42)
        np.save(numpy_data_filepaths(save_name + '_train', shape, output_dirname)[0], X_train)
        np.save(numpy_data_filepaths(save_name + '_train', shape, output_dirname)[1], y_train)
        np.save(numpy_data_filepaths(save_name + '_test', shape, output_dirname)[0], X_test)
        np.save(numpy_data_filepaths(save_name + '_test', shape, output_dirname)[1], y_test)
        print("Saved train/test split with shape (width, height):", shape, f"for {len(dataset_names)} datasets", dataset_names, f"({len(X_train)} training images, {len(X_test)} testing images)")
    return X, y.astype('float32')

def numpy_to_images_labels(X, y, prefix_name, columns=POINT_LABELS):
    # for now, just overwrite existing files if found
    print("writing to", custom_path(prefix_name))
    for i in range(len(X)):
        img = X[i]
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cv2.imwrite(custom_image_path(prefix_name, i), img)
    labels = pd.DataFrame(y, columns=columns)
    labels['frame_num'] = range(len(labels))
    labels.to_json(custom_label_path(prefix_name), orient='records')
    pass