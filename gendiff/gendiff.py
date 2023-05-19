from gendiff.parsing import parsing
from gendiff.formatters import format_stylish, format_plain
from gendiff.constants import ADDED, REMOVED, CHANGED, UNCHANGED, DICT

CHOOSE_FORMAT = {
    "stylish": format_stylish,
    "plain": format_plain,
}


def make_diff(dict_1, dict_2) -> dict:
    shared_keys = dict_1.keys() & dict_2.keys()
    dict1_keys = dict_1.keys() - dict_2.keys()
    dict2_keys = dict_2.keys() - dict_1.keys()

    diff = {}

    for key in shared_keys:
        child_1 = dict_1.get(key)
        child_2 = dict_2.get(key)

        if child_1 == child_2:
            diff[key] = {
                "status": UNCHANGED,
                "diff": {key: child_1},
            }
        elif isinstance(child_1, dict) and isinstance(child_2, dict):
            diff[key] = {
                "status": DICT,
                "diff": make_diff(child_1, child_2),
            }
        else:
            diff[key] = {
                "status": CHANGED,
                "diff_rem": {key: child_1},
                "diff_add": {key: child_2},
            }
    for key in dict1_keys:
        diff[key] = {
            "status": REMOVED,
            "diff": {key: dict_1[key]},
        }
    for key in dict2_keys:
        diff[key] = {
            "status": ADDED,
            "diff": {key: dict_2[key]},
        }
    return dict(sorted(diff.items()))


def generate_diff(file1, file2, format_name="stylish"):
    dict_1, dict_2 = parsing(file1, file2)
    diff = make_diff(dict_1, dict_2)
    return CHOOSE_FORMAT[format_name](diff)
