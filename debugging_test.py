import io
import sys
import pytest
from debugging import find_max, sort_list, calculate_average

def test_find_max():
    # Test correct functionality
    assert find_max([1, 3, 5, 2, 4]) == 5, "find_max should return the maximum number in the list"
    assert find_max([-1, -3, -5, -2, -4]) == -1, "find_max should work with negative numbers"
    assert find_max([100]) == 100, "find_max should work with a single-element list"
    assert find_max([]) is None, "find_max should return None for an empty list"

    # Test if print statements are used
    captured_output = io.StringIO()
    sys.stdout = captured_output
    find_max([1, 3, 5, 2, 4])
    sys.stdout = sys.__stdout__
    assert "max" in captured_output.getvalue().lower(), "Use print statements to debug find_max function"

def test_sort_list():
    # Test correct functionality
    assert sort_list([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9], "sort_list should correctly sort the list"
    assert sort_list([]) == [], "sort_list should handle empty lists"
    assert sort_list([1]) == [1], "sort_list should handle single-element lists"

    # Test if print is used for output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    sort_list([3, 1, 4, 1, 5])
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue().lower()
    assert "comparisons" in output and "swaps" in output, "Use print to output the number of comparisons and swaps"

def test_calculate_average():
    # Test correct functionality
    assert calculate_average([1, 2, 3, 4, 5]) == 3, "calculate_average should return the correct average"
    assert calculate_average([]) == 0, "calculate_average should return 0 for an empty list"
    assert calculate_average([1]) == 1, "calculate_average should work with a single-element list"
    assert round(calculate_average([1.5, 2.5, 3.5]), 2) == 2.5, "calculate_average should work with floating-point numbers"

    # Test if print statements are used
    captured_output = io.StringIO()
    sys.stdout = captured_output
    calculate_average([1, 2, 3, 4, 5])
    sys.stdout = sys.__stdout__
    assert "total" in captured_output.getvalue().lower() and "count" in captured_output.getvalue().lower(), "Use print statements to debug calculate_average function"

def run_tests():
    pytest.main([__file__])

if __name__ == "__main__":
    run_tests()
