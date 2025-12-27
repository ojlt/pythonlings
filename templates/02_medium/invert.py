"""
Invert Dictionary

Complete the function invert(data) where the input data is a dict. The
function should invert this dict, where the original keys become values and
the original values become keys.

Since multiple original keys might map to the same original value, the new
dictionary's values should be a list of keys. The items in this list should
be sorted in ascending order.

Examples:
    invert({"a": 1, "b": 2, "c": 1}) -> {1: ["a", "c"], 2: ["b"]}
    invert({"apple": "fruit", "banana": "fruit", "carrot": "vegetable"})
        -> {"fruit": ["apple", "banana"], "vegetable": ["carrot"]}
    invert({}) -> {}
    invert({"key1": "val1"}) -> {"val1": ["key1"]}
"""

# I AM NOT DONE


def invert(data):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_simple():
    data = {"a": 1, "b": 2, "c": 1}
    expected_result = {1: ["a", "c"], 2: ["b"]}
    actual_result = invert(data)
    assert actual_result == expected_result


def test_strings():
    data = {"apple": "fruit", "banana": "fruit", "carrot": "vegetable"}
    expected_result = {"fruit": ["apple", "banana"], "vegetable": ["carrot"]}
    actual_result = invert(data)
    assert actual_result == expected_result


def test_mixed():
    data = {1: "a", "b": 2, 3: "a", "d": 2}
    expected_result = {"a": [1, 3], 2: ["b", "d"]}
    actual_result = invert(data)
    assert actual_result == expected_result


def test_empty():
    data = {}
    expected_result = {}
    actual_result = invert(data)
    assert actual_result == expected_result


def test_single():
    data = {"key1": "val1"}
    expected_result = {"val1": ["key1"]}
    actual_result = invert(data)
    assert actual_result == expected_result


if __name__ == "__main__":
    test_simple()
    test_strings()
    test_mixed()
    test_empty()
    test_single()
    print("All tests passed!")
