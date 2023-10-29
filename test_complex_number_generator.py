import unittest
from complex_number_generator import random_complex_number_within_abs  # Replace 'your_module_name' with the actual name of your module

class TestRandomComplexNumber(unittest.TestCase):
    def test_random_complex_number_within_abs(self):
        # Test that generated complex number is within the specified absolute value is below
        # the _ is a way to repeat a block of code a specific number of times without needing 
        # to refer to the loop index or value. In other words, 'let's loop like normal loops, 
        # but there's no need for using a variable in the loop'
        for _ in range(100):
            random_num = random_complex_number_within_abs(5)
            self.assertLessEqual(abs(random_num), 5)

if __name__ == '__main__':
    unittest.main()
