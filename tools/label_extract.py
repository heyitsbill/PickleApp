import xml.etree.ElementTree as ET
import json
import os
from pathlib import Path


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
    metadata['task'] = {node.tag: node.text for node in root.find('meta').find('task')}
    metadata['dumped'] = root.find('meta').find('dumped').text
    return {'metadata': metadata, 'frames': frame_labels, 'start_frame': start_frame, 'end_frame': end_frame}

def extract_and_save_cvat_annotations(cvat_xml_path, output_dir, start_frame = None, end_frame = None, filename = None):
    input_path = Path(cvat_xml_path)
    annotations = extract_cvat_annotations(cvat_xml_path, start_frame, end_frame)
    input_filename = os.path.basename(input_path).split('.')[0]
    filename = input_filename if filename is None else filename
    output_path = Path(output_dir) / f'{filename}.json'
    with open(output_path, 'w') as f:
        json.dump(annotations, f)

def read_extracted_labels(label_path):
    with open(label_path, 'r') as f:
        labels = json.load(f)
    return labels
