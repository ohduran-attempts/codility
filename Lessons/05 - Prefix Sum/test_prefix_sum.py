import countdiv
import unittest


class TestCountDiv(unittest.TestCase):
    """Test CountDiv cases"""

    def test_1(self):
        """Proposed test 1."""
        A, B, K = 6, 11, 2
        expected_result = 3

        self.assertEqual(countdiv.countdiv(A, B, K), expected_result)

    def own_test_1(self):
        """Own Test 1."""
        A, B, K = 5, 10, 2
        expected_result = 3

        self.assertEqual(countdiv.countdiv(A, B, K), expected_result)


if '__name__' == '__main__':
    unittest.main()
