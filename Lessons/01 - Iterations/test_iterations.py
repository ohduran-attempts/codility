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

    def test_2(self):
        """Proposed test 2"""
        N = 9
        # Number 9 has binary representation 1001 and contains a binary gap of length 2.
        expected_result = 2

        self.assertEqual(expected_result, binary_gap(N))

    def test_3(self):
        """Proposed test 3"""
        N = 529
        # Number 529 has binary representation 1000010001
        # and contains two binary gaps: one of length 4 and one of length 3.
        expected_result = 4

        self.assertEqual(expected_result, binary_gap(N))

    def test_4(self):
        """Proposed test 4"""
        N = 32
        # Number 32 has binary representation 100000 and has no binary gaps.
        expected_result = 0

        self.assertEqual(expected_result, binary_gap(N))

    def test_5(self):
        """Proposed test 5."""
        N = 20
        # Number 20 has binary representation 10100 and contains one binary gap of length 1.
        expected_result = 1

        self.assertEqual(expected_result, binary_gap(N))

    def test_6(self):
        """Proposed test 6."""
        N = 15
        # Number 15 has binary representation 1111 and has no binary gaps.
        expected_result = 0

        self.assertEqual(expected_result, binary_gap(N))

    def own_test_1(self):
        """Own Test 1."""
        N = 33
        # N has binary representation 100001
        expected_result = 4

        self.assertEqual(expected_result, binary_gap(N))



if __name__ == '__main__':
    unittest.main()
