import unittest
import maxproductofthree


class TestMaxProductOfThree(unittest.TestCase):
    """Test Max Product Of 3 algorithm."""

    def test_1(self):
        """Test 1."""

        A = [-3, 1, 2, -2, 5, 6]
        expected_result = 60

        self.assertEqual(expected_result, maxproductofthree.maxproduct_ofthree(A))

    def test_2(self):
        """Test 2"""
        A = [-5, 5, -5, 4]
        expected_result = 125

        self.assertEqual(expected_result, maxproductofthree.maxproduct_ofthree(A))


if __name__ == '__main__':
    unittest.main()
