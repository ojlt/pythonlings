"""
Find Files by Extension

Complete the function find_files_by_extension(filesystem, extension). This
function takes a nested dictionary filesystem representing a file system
structure and a string extension (e.g., ".txt").

The function must recursively search the directory structure and return a
list of full paths (as strings) to all files that end with the given extension.
The paths should start from the root (/).

The structure of the filesystem dictionary is: It represents a directory.
It has a name (string) and children (list). children contains other
dictionaries, which can be either:
- a directory: {"name": "...", "type": "directory", "children": [...]}
- a file: {"name": "...", "type": "file"}

Examples:
    find_files_by_extension(fs_data, ".txt")
        -> ['/home/user/profile.txt', '/home/user/docs/notes.txt']
    find_files_by_extension(fs_data, ".pdf")
        -> ['/home/user/docs/report.pdf']
    find_files_by_extension(fs_data, ".log")
        -> ['/system.log']
    find_files_by_extension(fs_data, ".zip")
        -> []
"""

# I AM NOT DONE


def find_files_by_extension(filesystem, extension):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
TEST_FILESYSTEM = {
    "name": "/",
    "type": "directory",
    "children": [
        {
            "name": "home",
            "type": "directory",
            "children": [
                {
                    "name": "user",
                    "type": "directory",
                    "children": [
                        {"name": "profile.txt", "type": "file"},
                        {
                            "name": "docs",
                            "type": "directory",
                            "children": [
                                {"name": "notes.txt", "type": "file"},
                                {"name": "report.pdf", "type": "file"}
                            ]
                        }
                    ]
                }
            ]
        },
        {"name": "system.log", "type": "file"}
    ]
}


def test_txt_files():
    result = find_files_by_extension(TEST_FILESYSTEM, ".txt")
    expected = ['/home/user/profile.txt', '/home/user/docs/notes.txt']
    assert sorted(result) == sorted(expected)


def test_pdf_files():
    result = find_files_by_extension(TEST_FILESYSTEM, ".pdf")
    expected = ['/home/user/docs/report.pdf']
    assert result == expected


def test_log_files():
    result = find_files_by_extension(TEST_FILESYSTEM, ".log")
    expected = ['/system.log']
    assert result == expected


def test_no_matches():
    result = find_files_by_extension(TEST_FILESYSTEM, ".zip")
    expected = []
    assert result == expected


if __name__ == "__main__":
    test_txt_files()
    test_pdf_files()
    test_log_files()
    test_no_matches()
    print("All tests passed!")
