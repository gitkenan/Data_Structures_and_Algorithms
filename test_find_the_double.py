# What defines a good test? It's good communication,
# and good execution, just like any other file in any 
# other language. 
import unittest
from find_the_double import duplicate_numbers
class TestFindTheDouble(unittest.TestCase):
    def test_multiple_duplicate_numbers(self):
        arr1 = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 23, 23, 545, 3463, 235, 2363]
        expected_result1 = [5, 6, 23]
        self.assertIs(duplicate_numbers(arr1), expected_result1)
    
    def test_zero_duplicate_numbers(self):
        arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_result2 = []
        self.assertIs(duplicate_numbers(arr2), expected_result2)
    
    def test_one_element(self):
        arr3 = [42]
        expected_result3 = []
        self.assertIs(duplicate_numbers(arr3), expected_result3)
        
    def test_fully_duplicate_numbers(self):
        arr4 = [5, 5, 5, 5, 5]
        expected_result4 = [5]
        self.assertIs(duplicate_numbers(arr4), expected_result4)

if __name__ == "__main__":
    unittest.main()
