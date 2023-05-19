from gendiff.constants import ADDED, REMOVED, CHANGED, DICT, UNCHANGED


def edit_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    return value


def to_string(tree, depth=1):
    curr_prefix = UNCHANGED * depth
    prev_prefix = curr_prefix[:-4]
    result = []

    def to_str_dict(dictionary, deep=1):
        res = []
        for k, v in dictionary.items():
            if not isinstance(v, dict):
                v = edit_value(v)
                res.append(UNCHANGED * deep + curr_prefix + f"{k}: {v}")
            else:
                res.append(UNCHANGED * deep + curr_prefix + f"{k}: " + "{")
                res.append(prev_prefix + to_str_dict(v, deep + 1))
                res.append(UNCHANGED * deep + curr_prefix + "}")
        return "\n".join(res)

    def to_str_tree_dict(dictionary, status):
        for k, v in dictionary.items():
            if not any(isinstance(val, dict) for val in dictionary.values()):
                v = edit_value(v)
                result.append(prev_prefix + status + f"{k}: {v}")
            else:
                result.append(prev_prefix + status + f"{k}: " + "{")
                result.append(to_str_dict(v))
                result.append(curr_prefix + "}")

    for key, value in tree.items():
        if value["status"] == DICT:
            result.append(curr_prefix + f"{key}: " + "{")
            result.append(to_string(value["diff"], depth + 1))
        elif value["status"] == CHANGED:
            to_str_tree_dict(value["diff_rem"], status=REMOVED)
            to_str_tree_dict(value["diff_add"], status=ADDED)
        else:
            to_str_tree_dict(value["diff"], status=value["status"])

    result = "\n".join(result) + f"\n{prev_prefix}" + "}"
    return result


def format_stylish(diff: dict):
    return "{\n" + to_string(diff)
