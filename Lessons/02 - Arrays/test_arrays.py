from cyclic_rotation import cyclic_rotation
import unittest


class TestCyclicRotation(unittest.TestCase):
    """Test the Cyclic Rotation exercise."""

    def test_1(self):
        """Proposed Test 1."""
        pass

    def test_2(self):
        """Proposed Test 2."""
        A = [3, 8, 9, 7, 6]
        N = 1
        expected_result = [6, 3, 8, 9, 7]

        self.assertEqual(cyclic_rotation(A, N), expected_result)

    def test_3(self):
        """Proposed Test 3."""
        A = [3, 8, 9, 7, 6]
        N = 3
        expected_result = [9, 7, 6, 3, 8]

        self.assertEqual(cyclic_rotation(A, N), expected_result)

    def test_4(self):
        """Proposed Test 4."""
        A = [0, 0, 0]
        N = 1
        expected_result = A

        self.assertEqual(cyclic_rotation(A, N), expected_result)

    def test_5(self):
        """Proposed Test 5."""
        A = [1, 2, 3, 4]
        N = 4

        expected_result = A

        self.assertEqual(cyclic_rotation(A, N), expected_result)



if __name__ == '__main__':
    unittest.main()
