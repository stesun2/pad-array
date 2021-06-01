# Write unit tests!
import unittest
from pad_array import pad_array

class PadArrayTestCase(unittest.TestCase):
    """Test for pad_array.py"""

    def test_returns_empty_list(self):
        """Calls pad_array.py, returns an empty list"""
        self.assertEqual(len(pad([''],'', '')), [])
    
    def test_returns_min_size(self):
        """Calls pad_array.py, returns the length of min size """
        self.assertEqual()

    def test_returns_padded_list(self):
        """Calls pad_array.py, returns a padded list mode"""
        self.assertEqual()

    def test_returns_non_negative_int(self):
        """Calls pad_array.py, checks if min_size is non-negative integer"""
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()
