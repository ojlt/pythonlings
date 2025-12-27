"""
File Processor

Implement a set of classes that process different file types. This exercise
demonstrates polymorphism.

1. FileProcessor (Base Class):
   - Implement an __init__(self, filename).
   - Implement a method read(self) that raises a NotImplementedError.
   - Implement a method process(self) that raises a NotImplementedError.

2. CsvProcessor (Subclass of FileProcessor):
   - Implement read(self): Reads the CSV file. Each line is a row of comma-
     separated values. read should store a list of lists (rows) as an
     attribute (e.g., self.data).
   - Implement process(self): This method should:
     1. Call self.read() to ensure data is loaded.
     2. Assume the first row is a header.
     3. Return a list of dictionaries, where each dictionary maps header
        keys to row values.

3. JsonProcessor (Subclass of FileProcessor):
   - Implement read(self): Reads the JSON file and stores the loaded data
     (which will be a list of dictionaries) as an attribute (e.g., self.data).
   - Implement process(self): This method should:
     1. Call self.read() to ensure data is loaded.
     2. Simply return the loaded data, as it's already in the target format.

You will also need to complete the function process_files(processors) that
takes a list of FileProcessor objects and returns a list containing the
processed data from each one.
"""

# I AM NOT DONE


class FileProcessor:
    pass


class CsvProcessor(FileProcessor):
    pass


class JsonProcessor(FileProcessor):
    pass


def process_files(processors):
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

    # Create CSV file
    csv_file = os.path.join(data_dir, "data.csv")
    with open(csv_file, "w") as f:
        f.write("name,age,city\\n")
        f.write("Alice,30,London\\n")
        f.write("Bob,25,Paris\\n")

    # Create JSON file
    json_file = os.path.join(data_dir, "data.json")
    json_data = [
        {"name": "Charlie", "age": 35, "city": "Berlin"},
        {"name": "Diana", "age": 28, "city": "Rome"}
    ]
    with open(json_file, "w") as f:
        json.dump(json_data, f)

    return csv_file, json_file


def test_csv_processor():
    csv_file, _ = setup_test_files()
    processor = CsvProcessor(csv_file)
    result = processor.process()

    expected = [
        {"name": "Alice", "age": "30", "city": "London"},
        {"name": "Bob", "age": "25", "city": "Paris"}
    ]
    assert result == expected


def test_json_processor():
    _, json_file = setup_test_files()
    processor = JsonProcessor(json_file)
    result = processor.process()

    expected = [
        {"name": "Charlie", "age": 35, "city": "Berlin"},
        {"name": "Diana", "age": 28, "city": "Rome"}
    ]
    assert result == expected


def test_process_files():
    csv_file, json_file = setup_test_files()
    processors = [CsvProcessor(csv_file), JsonProcessor(json_file)]
    results = process_files(processors)

    assert len(results) == 2
    assert len(results[0]) == 2  # CSV has 2 data rows
    assert len(results[1]) == 2  # JSON has 2 items


if __name__ == "__main__":
    test_csv_processor()
    test_json_processor()
    test_process_files()
    print("All tests passed!")
