import json


def generate_diff(file1, file2):
    difference = ''
    first_file = dict(json.load(open(file1)))
    second_file = dict(json.load(open(file2)))

    shared_keys = sorted(first_file.keys() & second_file.keys())
    file1_keys = sorted(first_file.keys() - second_file.keys())
    file2_keys = sorted(second_file.keys() - first_file.keys())

    
    for key in shared_keys:
        if first_file[key] == second_file[key]:
            difference += f"  {key}: {first_file[key]}\n"
        else:
            difference += f"- {key}: {first_file[key]}\n"
            difference += f"+ {key}: {second_file[key]}\n"
    for key in file1_keys:
        difference += f"- {key}: {first_file[key]}\n"
    for key in file2_keys:
        difference += f"+ {key}: {second_file[key]}\n"

    return "{\n" + difference.lower() + "}"