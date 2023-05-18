from gendiff.constants import ADDED, REMOVED, CHANGED, UNCHANGED, DICT, PREFIX


def edit_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    return value


def to_string(tree, depth=1):
    curr_prefix = PREFIX * depth
    prev_prefix = curr_prefix[:-len(PREFIX)]
    result = []

    def to_str_dict(dictionary, deep=1):
        res = []
        for k, v in dictionary.items():
            if not isinstance(v, dict):
                v = edit_value(v)
                res.append(PREFIX * deep + curr_prefix + f"{k}: {v}")
            else:
                res.append(PREFIX * deep + curr_prefix + f"{k}: " + "{")
                res.append(prev_prefix + to_str_dict(v, deep + 1))
                res.append(PREFIX * deep + curr_prefix + "}")
        return "\n".join(res)

    def to_str_tree_dict(dictionary, status):
        for k, v in dictionary.items():
            if not any(isinstance(i, dict) for i in dictionary.values()):
                v = edit_value(v)
                result.append(prev_prefix + status + f"{k}: {v}")
            else:
                result.append(prev_prefix + status + f"{k}: " + "{")
                result.append(to_str_dict(v))
                result.append(curr_prefix + "}")

    for key, value in tree.items():
        status = value["status"]
        if status == DICT:
            result.append(curr_prefix + f"{key}: " + "{")
            result.append(to_string(value["diff"], depth + 1))
        elif status == CHANGED:
            to_str_tree_dict(value["diff_rem"], status=REMOVED)
            to_str_tree_dict(value["diff_add"], status=ADDED)
        elif status == UNCHANGED:
            to_str_tree_dict(value["diff"], status=UNCHANGED)
        else:
            to_str_tree_dict(value["diff"], status=value["status"])

    result = "\n".join(result) + f"\n{prev_prefix}" + "}"
    return result


def stylish(diff: dict):
    return "{\n" + to_string(diff)
