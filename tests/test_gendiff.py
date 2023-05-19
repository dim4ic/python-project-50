import pytest
from gendiff import generate_diff
from tests.fixtures.test_results import RESULT_PLAIN, RESULT_TREE, RESULT_STAT


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
def format_name():
    format_name = {
        "stylish": "stylish",
        "plain": "plain",
    }
    return format_name


def test_generate_diff(paths, format_name):
    result_diff_json = generate_diff(
        paths["json1"],
        paths["json2"],
        format_name["stylish"],
    )
    result_diff_yml = generate_diff(
        paths["yml1"],
        paths["yml2"],
        format_name["stylish"],
    )
    result_diff_json_tree = generate_diff(
        paths["tree_json1"],
        paths["tree_json2"],
        format_name["stylish"],
    )
    result_diff_yml_tree = generate_diff(
        paths["tree_yml1"],
        paths["tree_yml2"],
        format_name["stylish"],
    )
    result_diff_json_tree_stat = generate_diff(
        paths["tree_json1"],
        paths["tree_json2"],
        format_name["plain"],
    )
    result_diff_yml_tree_stat = generate_diff(
        paths["tree_yml1"],
        paths["tree_yml2"],
        format_name["plain"],
    )
    assert result_diff_json == RESULT_PLAIN
    assert result_diff_yml == RESULT_PLAIN
    assert result_diff_json_tree == RESULT_TREE
    assert result_diff_yml_tree == RESULT_TREE
    assert result_diff_json_tree_stat == RESULT_STAT
    assert result_diff_yml_tree_stat == RESULT_STAT