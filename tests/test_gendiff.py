import pytest
from gendiff import generate_diff
from gendiff.parsing import parsing


@pytest.fixture
def paths():
    paths = {
        "json1": "tests/fixtures/file1.json",
        "json2": "tests/fixtures/file2.json",
        "yml1": "tests/fixtures/file1.yml",
        "yml2": "tests/fixtures/file2.yml",
        "tree_json1": "tests/fixtures/tree1.json",
        "tree_json2": "tests/fixtures/tree2.json",
        "tree_yml1": "tests/fixtures/tree1.yml",
        "tree_yml2": "tests/fixtures/tree2.yml",
    }
    return paths


@pytest.fixture
def expected_value():
    with open("tests/fixtures/expected_value") as file:
        expected_value = file.read()
    return expected_value


@pytest.fixture
def expected_value_tree():
    with open("tests/fixtures/expected_value_tree") as file:
        expected_value_tree = file.read()
    return expected_value_tree


def test_generate_diff(paths, expected_value, expected_value_tree):
    result_diff_json = str(generate_diff(paths["json1"], paths["json2"]))
    result_diff_yml = str(generate_diff(paths["yml1"], paths["yml2"]))
    result_diff_json_tree = str(generate_diff(paths["tree_json1"],
                                              paths["tree_json2"]))
    result_diff_yml_tree = str(generate_diff(paths["tree_yml1"],
                                             paths["tree_yml2"]))
    assert result_diff_json == expected_value
    assert result_diff_yml == expected_value
    assert result_diff_json_tree == expected_value_tree
    assert result_diff_yml_tree == expected_value_tree