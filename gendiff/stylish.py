from gendiff.constants import ADDED, REMOVED, CHANGED, UNCHANGED, DICT, PREFIX


def is_plain_dict(dictionary):
    if isinstance(dictionary, dict):
        return not any(isinstance(i, dict) for i in dictionary.values())
    return True


def to_string(tree, depth=1):
    curr_prefix = PREFIX * depth
    prev_prefix = curr_prefix[:-len(PREFIX)]
    result = []


    def to_str_dict(dictionary, deep=1):
        res = []
        for k, v in dictionary.items():
            if not isinstance(v, dict):
                res.append(PREFIX * deep + curr_prefix + f"{k}: {v}")
            else:
                res.append(PREFIX * deep + curr_prefix + f"{k}: " + "{")
                res.append(prev_prefix + to_str_dict(v, deep + 1))
                res.append(PREFIX * deep + curr_prefix + "}")
        return "\n".join(res).lower()

    def to_str_tree_dict(dictionary, status):
        for k, v in dictionary.items():
            if is_plain_dict(dictionary):
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

    result = "\n".join(result).lower() + f"\n{prev_prefix}" + "}"
    return result


def stylish(diff: dict):
    return "{\n" + to_string(diff)