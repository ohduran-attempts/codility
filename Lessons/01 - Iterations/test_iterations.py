from iterations import binary_gap
import unittest


class TestCases(unittest.TestCase):
    """Test Case."""

    def test_1(self):
        """Proposed test"""
        N = 1041
        # N has binary representation 10000010001
        expected_result = 5

        self.assertEqual(expected_result, binary_gap(N))


if __name__ == '__main__':
    unittest.main()
