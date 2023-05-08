import pytest
from gendiff import generate_diff


@pytest.fixture
def file1():
	return "tests/fixtures/file1.json"


@pytest.fixture
def file2():
	return "tests/fixtures/file2.json"


@pytest.fixture
def expected_value_json():
	with open("tests/fixtures/expected_value_json") as file:
		expected_value_json = file.read()
	return expected_value_json


def test_generate_diff(file1, file2, expected_value_json):
	result = str(generate_diff(file1, file2))
	assert result == expected_value_json