"""
Most Frequent Common Word

Complete the function most_frequent_common_word(filename1, filename2) to
return the most frequent word in common across two text files filename1 and
filename2, and its average frequency.

The most frequent word is the word that:
- occurs in both text files and
- has the highest average frequency across the two text files.

The function should return a tuple with 2 elements: the first is the most
frequent common word (a str), the second is the average frequency (a float).

For example, assume filename1 and filename2 have only two words in common
(e.g. good, bad). The word good occurs 6 times in filename1 and 4 times in
filename2. The word bad occurs 7 times in filename1 and once in filename2.
Therefore, the average frequency for good is 5 (i.e. (6+4)/2) and for bad is
4 (i.e. (7+1)/2). Therefore, the function should return the tuple ("good", 5).

You can assume that each word in the file is separated by a space. You can
also assume that the texts contain only words consisting of all lowercase
alphabetic letters (a to z).

Assume that filename1 and filename2 always points to valid text files.
"""

# I AM NOT DONE


def most_frequent_common_word(filename1, filename2):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
import os


def setup_test_files():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(test_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    # Create file1.txt
    file1 = os.path.join(data_dir, "file1.txt")
    with open(file1, "w") as f:
        f.write("the the the the cat sat on the the the mat the dog the")

    # Create file2.txt
    file2 = os.path.join(data_dir, "file2.txt")
    with open(file2, "w") as f:
        f.write("the the cat is on the the the mat")

    return file1, file2


def test_common_word():
    file1, file2 = setup_test_files()
    word, freq = most_frequent_common_word(file1, file2)
    assert word == "the"
    assert freq == 9.5  # (11 + 8) / 2


if __name__ == "__main__":
    test_common_word()
    print("All tests passed!")
