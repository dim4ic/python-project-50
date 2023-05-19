from gendiff.constants import ADDED, REMOVED, CHANGED, DICT, COMPLEX


def make_phrase(phrase_type, path="", value1="", value2=""):
    phrases = {
        "removed": f"Property {path} was removed",
        "added": f"Property {path} was added with value: {value2}",
        "updated": f"Property {path} was updated. From {value1} to {value2}",
    }
    return phrases[phrase_type]


def is_tree(dictionary):
    if isinstance(dictionary, dict):
        return any(isinstance(value, dict) for value in dictionary.values())
    return dictionary


def edit_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    return f"'{value}'"


def make_value(value, key):
    if is_tree(value):
        return COMPLEX
    return edit_value(value[key])


def format_plain(diff: dict, node=""):
    result = []
    for key, value in diff.items():
        path = f"'{key}'"
        status = value["status"]
        if status == ADDED:
            value2 = make_value(value["diff"], key)
            phrase = make_phrase("added", path, value2=value2)
            result.append(phrase)
        elif status == REMOVED:
            value2 = make_value(value["diff"], key)
            phrase = make_phrase("removed", path, value2=value2)
            result.append(phrase)
        elif status == CHANGED:
            value1 = make_value(value["diff_rem"], key)
            value2 = make_value(value["diff_add"], key)
            phrase = make_phrase("updated", path, value1=value1, value2=value2)
            result.append(phrase)
        elif status == DICT:
            result.append(format_plain(value["diff"]))

    return "\n".join(result)