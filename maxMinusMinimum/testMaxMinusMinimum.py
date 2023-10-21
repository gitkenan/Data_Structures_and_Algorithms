import unittest

def get_absolute_difference(arrayOfNumbers):
    if len(arrayOfNumbers) < 2:
        return 0
    return abs(max(arrayOfNumbers) - min(arrayOfNumbers))

class TestGetAbsoluteDifference(unittest.TestCase):
    def test_positive_numbers(self):
        result = get_absolute_difference([5, 3, 9, 1, 7])
        self.assertEqual(result, 8)

    def test_negative_numbers(self):
        result = get_absolute_difference([-5, -3, -9, -1, -7])
        self.assertEqual(result, 8)

    def test_mixed_numbers(self):
        result = get_absolute_difference([-5, 3, -9, 1, 7])
        self.assertEqual(result, 16)

    def test_empty_list(self):
        result = get_absolute_difference([])
        self.assertEqual(result, 0)

    def test_single_element(self):
        result = get_absolute_difference([42])
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()

