import unittest
from find_largest_and_smallest import outer_values

class TestOuterValues(unittest.TestCase):

    def test_outer_values_output_format(self):
        # Test with a list of integers
        unsorted_arr = [4, 135135, 12, 325, 2, 89712398, 874, 8273464223, 87234627834, 293479328, 38745623789479783, 2374673, 87236472374, 6743]
        result = outer_values(unsorted_arr)
        
        # Check if the result is a string
        self.assertTrue(isinstance(result, str))

        # Check if the expected strings are present in the result
        self.assertIn("The biggest is", result)
        self.assertIn("and the smallest is", result)

if __name__ == '__main__':
    unittest.main()
