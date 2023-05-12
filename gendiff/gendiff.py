import json


def generate_diff(file1, file2):
    difference = []
    first_file = dict(json.load(open(file1)))
    second_file = dict(json.load(open(file2)))

    shared_keys = sorted(first_file.keys() & second_file.keys())
    file1_keys = sorted(first_file.keys() - second_file.keys())
    file2_keys = sorted(second_file.keys() - first_file.keys())

    for key in shared_keys:
        if first_file[key] == second_file[key]:
            diff_shared = f"    {key}: {first_file[key]}"
            difference.append(diff_shared)
        else:
            diff_shared1 = f"  - {key}: {first_file[key]}"
            difference.append(diff_shared1)
            diff_shared2 = f"  + {key}: {second_file[key]}"
            difference.append(diff_shared2)
    for key in file1_keys:
        diff_file1 = f"  - {key}: {first_file[key]}"
        difference.append(diff_file1)
    for key in file2_keys:
        diff_file2 = f"  + {key}: {second_file[key]}"
        difference.append(diff_file2)

    sort_difference = sorted(difference, key=lambda x: x[4])
    final_diff = ['{'] + sort_difference + ['}']
    diff_string = '\n'.join(final_diff)
    final_diff_string = diff_string.replace('"', '')
    return final_diff_string
