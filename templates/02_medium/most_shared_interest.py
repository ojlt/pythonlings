"""
Most Shared Interest

Complete the function most_shared_interest(json_filename) that loads a JSON
database given by json_filename and returns information about the pair of
students who are members in the same society the most number of times.

The input JSON file is expected to have the following structure:
{
    "students": {"1": "John", "2": "Paul", "3": "Ringo"},
    "societies": {"1": "Badminton", "2": "Golf", "3": "Hockey"},
    "memberships": [
        {"society": "1", "student": "1"},
        {"society": "1", "student": "2"},
        ...
    ]
}

The function should return a dict with two keys:
- "pair": The value should be a list containing the name of the two students
  who co-occur in the most number of societies.
- "societies": The value should be a list containing the list of society names
  that the pair of students share in common.

Both the list of "pair" and "societies" should be sorted in ascending
alphabetical order.

You can assume that all students and societies have different names, and that
the given JSON file will always exist, and that the JSON file structure will
always be valid.
"""

# I AM NOT DONE


def most_shared_interest(json_filename):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
import json
import os


def setup_test_files():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(test_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    # Create toy.json
    toy_data = {
        "students": {"1": "John", "2": "Paul", "3": "Ringo"},
        "societies": {"1": "Badminton", "2": "Tennis", "3": "Hockey"},
        "memberships": [
            {"society": "1", "student": "1"},
            {"society": "1", "student": "2"},
            {"society": "1", "student": "3"},
            {"society": "2", "student": "1"},
            {"society": "2", "student": "3"},
            {"society": "3", "student": "1"},
            {"society": "3", "student": "3"}
        ]
    }

    toy_file = os.path.join(data_dir, "toy.json")
    with open(toy_file, "w") as f:
        json.dump(toy_data, f)

    return toy_file


def test_toy():
    toy_file = setup_test_files()
    best_friends = most_shared_interest(toy_file)

    expected_output = {
        "pair": ["John", "Ringo"],
        "societies": ["Badminton", "Hockey", "Tennis"],
    }

    assert best_friends["pair"] == expected_output["pair"]
    assert best_friends["societies"] == expected_output["societies"]


if __name__ == "__main__":
    test_toy()
    print("All tests passed!")
