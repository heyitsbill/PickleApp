import xml.etree.ElementTree as ET
import json
import os
from pathlib import Path
import pandas as pd


def extract_cvat_annotations(cvat_xml_path, start_frame = None, end_frame = None):
    tree = ET.parse(cvat_xml_path)
    root = tree.getroot()
    court_nodes = root.findall('track[@label="Left Court"]')
    court_nodes = root.findall('track[@label="Right Court"]') if not court_nodes else court_nodes
    frame_labels = {}
    for court_node in court_nodes:
        for skeleton in court_node:
            frame = int(skeleton.attrib['frame'])
            if start_frame is not None and frame < start_frame:
                continue
            if end_frame is not None and frame > end_frame:
                continue

            labels = {}
            for child in skeleton:
                if child.tag == 'points':
                    point_data = child.attrib
                    point_data['points'] = [float(x) for x in point_data['points'].split(',')]
                    point_data['label'] = int(point_data['label'])
                    point_data['occluded'] = int(point_data['occluded'])
                    point_data['outside'] = int(point_data['outside'])
                    labels[int(child.attrib['label'])] = point_data
                elif child.tag == 'attribute':
                    labels[child.attrib['name']] = child.text
            frame_labels[frame] = labels
    metadata = {}
    metadata['task'] = {node.tag: node.text for node in root.find('meta').find('task')} if root.find('meta').find('task') is not None else None
    metadata['dumped'] = root.find('meta').find('dumped').text
    return {'metadata': metadata, 'frames': frame_labels, 'start_frame': start_frame, 'end_frame': end_frame}

def extract_and_save_cvat_annotations(cvat_xml_path, output_dir, start_frame = None, end_frame = None, filename = None):
    input_path = Path(cvat_xml_path)
    annotations = extract_cvat_annotations(cvat_xml_path, start_frame, end_frame)
    input_filename = os.path.basename(input_path).split('.')[0]
    filename = input_filename if filename is None else filename
    output_path = Path(output_dir) / f'{filename}.json'
    annotations['filename'] = filename
    with open(output_path, 'w') as f:
        json.dump(annotations, f)

def read_extracted_labels(label_path):
    with open(label_path, 'r') as f:
        labels = json.load(f)
    return labels

def labels_to_df(labels):
    df = pd.DataFrame(labels['frames']).T
    return df

def labels_to_simple_df(labels, points_only = False, name = None):
    """
    Convert labels to a dataframe
    """
    frame_labels = labels['frames']
    new_labels = {}
    for frame, labels in frame_labels.items():
        normalized_labels = {}
        for label_num in [str(num) for num in range(1,11)]:
            normalized_labels[label_num + '_x'] = labels[label_num]['points'][0]
            normalized_labels[label_num + '_y'] = labels[label_num]['points'][1]
            if not points_only:
                normalized_labels[label_num + '_occluded'] = labels[label_num]['occluded']
                normalized_labels[label_num + '_outside'] = labels[label_num]['outside']
        normalized_labels['frame_num'] = frame
        new_labels[frame] = normalized_labels
    df = pd.DataFrame(new_labels).T
    if name is not None:
        df['name'] = name+'_'+df['frame_num'].astype(str)
        df.set_index('name', inplace=True)
    return df

def group_points_by_2(points):
    # create list of points grouped by 2
    grouped_points = []
    for i in range(0, len(points), 2):
        grouped_points.append(points[i:i+2])
    return grouped_points

def scale_down_points(points, scales):
    scaled_points = [[p[0] * scales[0], p[1] * scales[1]] for p in points]

def df_labels_to_point_list(labels):
    """
    Convert the dataframe to points
    """
    labels = pd.DataFrame(labels)
    labels['point_1'] = labels[['1_x', '1_y']].values.tolist()
    labels['point_2'] = labels[['2_x', '2_y']].values.tolist()
    labels['point_3'] = labels[['3_x', '3_y']].values.tolist()
    labels['point_4'] = labels[['4_x', '4_y']].values.tolist()
    labels['point_5'] = labels[['5_x', '5_y']].values.tolist()
    labels['point_6'] = labels[['6_x', '6_y']].values.tolist()
    labels['point_7'] = labels[['7_x', '7_y']].values.tolist()
    labels['point_8'] = labels[['8_x', '8_y']].values.tolist()
    labels['point_9'] = labels[['9_x', '9_y']].values.tolist()
    labels['point_10'] = labels[['10_x', '10_y']].values.tolist()
    return labels[['point_1', 'point_2', 'point_3', 'point_4', 'point_5', 'point_6', 'point_7', 'point_8', 'point_9', 'point_10']]
