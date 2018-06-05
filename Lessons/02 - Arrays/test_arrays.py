#!environment/bin/python3
from cyclic_rotation import cyclic_rotation
from oddoccurrences import odd_occurrences
import unittest


class TestCyclicrotation(unittest.TestCase):
    """Test the Cyclic Rotation exercise."""

    def test_1(self):
        """Proposed Test 1."""
        pass

    def test_2(self):
        """Proposed Test 2."""
        A = [3, 8, 9, 7, 6]
        K = 1
        expected_result = [6, 3, 8, 9, 7]

        self.assertEqual(cyclic_rotation(A, K), expected_result)

    def test_3(self):
        """Proposed Test 3."""
        A = [3, 8, 9, 7, 6]
        K = 3
        expected_result = [9, 7, 6, 3, 8]

        self.assertEqual(cyclic_rotation(A, K), expected_result)

    def test_4(self):
        """Proposed Test 4."""
        A = [0, 0, 0]
        K = 1
        expected_result = A

        self.assertEqual(cyclic_rotation(A, K), expected_result)

    def test_5(self):
        """Proposed Test 5."""
        A = [1, 2, 3, 4]
        K = 4

        expected_result = A

        self.assertEqual(cyclic_rotation(A, K), expected_result)

    def own_test_1(self):
        """Own Test 1."""
        A = [1, 2]
        K = 4

        expected_result = A

        self.assertEqual(cyclic_rotation(A, K), expected_result)

    def own_test_2(self):
        """Own Test 2."""
        A = [1, 2]
        K = 3

        expected_result = [2, 1]

        self.assertEqual(cyclic_rotation(A, K), expected_result)

    def own_test_3(self):
        """Own Test 3."""
        A = [1]
        K = 30

        expected_result = A

        self.assertEqual(cyclic_rotation(A, K), expected_result)


class TestOddOccurrences(unittest.TestCase):
    """Test Odd Occurrences algorithm."""

    def test_1(self):
        """Proposed Test 1."""
        A = [9, 3, 9, 3, 9, 7, 9]
        expected_result = 7

        self.assertEqual(odd_occurrences(A), expected_result)

    def own_test_1(self):
        """Own Test 1."""
        A = [42]
        expected_result = 42

        self.assertEqual(odd_occurrences(A), expected_result)


if __name__ == '__main__':
    unittest.main()
