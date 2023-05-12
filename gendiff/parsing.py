import os
import json
import yaml


def parsing(file1, file2):
    file1_ext = os.path.splitext(file1)
    file2_ext = os.path.splitext(file2)
    if (file1_ext and file2_ext) == '.json':
        first_file = json.load(open(file1))
        second_file = json.load(open(file2))
    if (file1_ext and file2_ext) == '.yaml' or '.yml':
        first_file = yaml.safe_load(open(file1))
        second_file = yaml.safe_load(open(file2))
    return dict(first_file), dict(second_file)
