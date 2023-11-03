# What defines a good test? It's good communication,
# and good execution, just like any other file in any 
# other language. 
import unittest
from find_the_double import duplicate_numbers
class TestFindTheDouble(unittest.test_case):
    def test_duplicate_numbers():
        # Test case 1: Array with multiple duplicates
        arr1 = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 23, 23, 545, 3463, 235, 2363]
        expected_result1 = [5, 6, 23]
        assert duplicate_numbers(arr1) == expected_result1, "Test case 1 failed"
    
        # Test case 2: Array with no duplicates
        arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_result2 = []
        assert duplicate_numbers(arr2) == expected_result2, "Test case 2 failed"
    
        # Test case 3: Array with a single element (no duplicates)
        arr3 = [42]
        expected_result3 = []
        assert duplicate_numbers(arr3) == expected_result3, "Test case 3 failed"
    
        # Test case 4: Array with all elements being duplicates
        arr4 = [5, 5, 5, 5, 5]
        expected_result4 = [5]
        assert duplicate_numbers(arr4) == expected_result4, "Test case 4 failed"
    
    print("All test cases passed")

if __name__ == "__main__":
    unittest.main()
