import os
import json
import yaml


def parsing(file1, file2):
    file1_ext = os.path.splitext(file1)
    file2_ext = os.path.splitext(file2)
    if (file1_ext and file2_ext) == '.json':
        dict_1 = json.load(open(file1))
        dict_2 = json.load(open(file2))
    if (file1_ext and file2_ext) == '.yaml' or '.yml':
        dict_1 = yaml.safe_load(open(file1))
        dict_2 = yaml.safe_load(open(file2))
    return dict(dict_1), dict(dict_2)
