"""
Get Error Summary

Complete the function get_error_summary(logfile) that reads a text file
given by logfile and returns a summary of all "ERROR" level messages.

Each line in the log file follows the format:
    [TIMESTAMP] [LEVEL] MESSAGE

The function should return a dictionary where:
- Keys are the unique MESSAGE strings from "ERROR" logs.
- Values are the integer count of how many times that "ERROR" message appeared.

The function should ignore "INFO" and "WARNING" logs.

Example:
    get_error_summary("access.log") should return:
    {
        "Failed to connect to database": 3,
        "User login failed: user_xyz": 2,
        "Disk space low": 1,
        "Null pointer exception at com.example.Module:42": 1
    }
"""

# I AM NOT DONE


def get_error_summary(logfile):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
import os

# Create test log file
TEST_LOG_CONTENT = """[2024-01-15 10:23:45] [INFO] Application started
[2024-01-15 10:23:46] [ERROR] Failed to connect to database
[2024-01-15 10:23:47] [WARNING] High memory usage detected
[2024-01-15 10:23:48] [ERROR] User login failed: user_xyz
[2024-01-15 10:23:49] [INFO] Cache cleared
[2024-01-15 10:23:50] [ERROR] Failed to connect to database
[2024-01-15 10:23:51] [ERROR] Disk space low
[2024-01-15 10:23:52] [ERROR] Failed to connect to database
[2024-01-15 10:23:53] [ERROR] User login failed: user_xyz
[2024-01-15 10:23:54] [ERROR] Null pointer exception at com.example.Module:42
[2024-01-15 10:23:55] [INFO] Application shutdown"""


def setup_test_file():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    test_file = os.path.join(test_dir, "data", "access.log")
    os.makedirs(os.path.dirname(test_file), exist_ok=True)
    with open(test_file, "w") as f:
        f.write(TEST_LOG_CONTENT)
    return test_file


def test_error_summary():
    test_file = setup_test_file()
    result = get_error_summary(test_file)
    expected = {
        "Failed to connect to database": 3,
        "User login failed: user_xyz": 2,
        "Disk space low": 1,
        "Null pointer exception at com.example.Module:42": 1
    }
    assert result == expected


if __name__ == "__main__":
    test_error_summary()
    print("All tests passed!")
