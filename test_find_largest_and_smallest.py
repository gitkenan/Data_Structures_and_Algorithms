import unittest
from find_largest_and_smallest import outer_values

class TestOuterValues(unittest.TestCase):

    def test_outer_values_are_correct(self):
        unsorted_arr = [4, 135135, 12, 325, 2, 89712398, 874, 8273464223, 87234627834, 293479328, 38745623789479783, 2374673, 87236472374, 6743]
        result = outer_values(unsorted_arr)
        
        # The spaces around the numbers are to be sure
        # that we are checking the result and not a part
        # of one of the numbers (2 is present in the largest)
        self.assertIn(" 2 ", result)
        self.assertIn(" 38745623789479783 ", result)
    
    def test_outer_values_returns_string(self):
        unsorted_arr = [4, 135135, 12, 325, 2, 89712398, 874, 8273464223, 87234627834, 293479328, 38745623789479783, 2374673, 87236472374, 6743]
        result = outer_values(unsorted_arr)
        
        self.assertTrue(isinstance(result, str))

        self.assertIn("The biggest is", result)
        self.assertIn("and the smallest is", result)

if __name__ == '__main__':
    unittest.main()
