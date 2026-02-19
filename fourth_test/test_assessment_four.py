import pytest
from assessment_four import *


# ========= BASIC TESTS =========

def test_count_unique_elements():
    assert count_unique_elements([1, 2, 2, 3]) == 3
    assert count_unique_elements([]) == 0


def test_merge_dictionaries():
    assert merge_dictionaries({"a": 1}, {"a": 2, "b": 3}) == {"a": 2, "b": 3}


def test_format_student_report():
    result = format_student_report("Alex", [70, 80, 75])
    assert "Alex" in result
    assert "75.00" in result


def test_compress_string():
    assert compress_string("aaabbc") == "a3b2c1"
    assert compress_string("") == ""


# ======= INTERMEDIATE TESTS =======

def test_group_by_length():
    words = ["hi", "cat", "dog", "a"]
    expected = {
        2: ["hi"],
        3: ["cat", "dog"],
        1: ["a"]
    }
    assert group_by_length(words) == expected


def test_reverse_list_recursively():
    assert reverse_list_recursively([1, 2, 3]) == [3, 2, 1]
    assert reverse_list_recursively([]) == []


def test_rotate_matrix_90():
    matrix = [
        [1, 2],
        [3, 4]
    ]
    assert rotate_matrix_90(matrix) == [
        [3, 1],
        [4, 2]
    ]


# ========= ADVANCED TESTS =========

def test_flatten_nested_list():
    assert flatten_nested_list([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]


def test_sum_nested_numbers():
    assert sum_nested_numbers([1, [2, [3, 4]], 5]) == 15


def test_generate_pascal_row():
    assert generate_pascal_row(0) == [1]
    assert generate_pascal_row(3) == [1, 3, 3, 1]

print(count_unique_elements([1, 2, 2, 3]))
