# =========================
# Assessment 4
# =========================


# ========= BASIC =========

def count_unique_elements(items):
    """Return the number of unique elements in the list."""
    unique_items =[]
    for i in items:
        if i not in unique_items:
            unique_items.append(i)
    return len(unique_items)


def merge_dictionaries(dict1, dict2):
    """Merge two dictionaries, overriding values from the first with the second."""
    pass


def format_student_report(name, marks):
    """Return a formatted report showing a student's name and average mark."""
    pass


def compress_string(text):
    """Compress a string by counting consecutive characters."""
    pass


# ======= INTERMEDIATE =======

def group_by_length(words):
    """Group words into a dictionary based on their length."""
    pass


def reverse_list_recursively(items):
    """Reverse a list using recursion."""
    pass


def rotate_matrix_90(matrix):
    """Rotate a square matrix 90 degrees clockwise."""
    pass


# ========= ADVANCED =========

def flatten_nested_list(nested):
    """Flatten a nested list of arbitrary depth using recursion."""
    pass


def sum_nested_numbers(nested):
    """Return the sum of all numbers in a nested list using recursion."""
    pass


def generate_pascal_row(n):
    """Return the nth row of Pascal's Triangle using recursion."""
    pass
