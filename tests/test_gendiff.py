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
	}
	return paths


@pytest.fixture
def expected_value():
	with open("tests/fixtures/expected_value") as file:
		expected_value = file.read()
	return expected_value


def test_generate_diff(paths, expected_value):
	result_diff_json = str(generate_diff(paths["json1"], paths["json2"]))
	result_diff_yml = str(generate_diff(paths["yml1"], paths["yml2"]))
	assert result_diff_json == expected_value
	assert result_diff_yml == expected_value