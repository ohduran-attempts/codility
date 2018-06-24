import countdiv, passingcars, DNA
import unittest


class TestCountDiv(unittest.TestCase):
    """Test CountDiv cases"""

    def test_1(self):
        """Proposed test 1."""
        A, B, K = 6, 11, 2
        expected_result = 3

        self.assertEqual(countdiv.countdiv(A, B, K), expected_result)

    def test_2(self):
        """Own Test 2."""
        A, B, K = 1, 1, 11
        expected_result = 0

        self.assertEqual(countdiv.countdiv(A, B, K), expected_result)

    def test_3(self):
        """Proposed Test 3."""
        A, B, K = 11, 345, 17
        expected_result = 20
        self.assertEqual(countdiv.countdiv(A, B, K), expected_result)

    def own_test_1(self):
        """Own Test 1."""
        A, B, K = 5, 10, 2
        expected_result = 3

        self.assertEqual(countdiv.countdiv(A, B, K), expected_result)

    def own_test_2(self):
        A, B = 6, 12
        for K in range(2, 7):
            if K == 5:
                expected_result = 1
                self.assertEqual(countdiv.countdiv(A, B, K), expected_result)
            else:
                expected_result = (B - A) // K + 1
                self.assertEqual(countdiv.countdiv(A, B, K), expected_result)


class TestPassingCars(unittest.TestCase):
    """Test passingCars algorithm."""

    def test_1(self):
        A = [0, 1, 0, 1, 1]
        expected_result = 5
        self.assertEqual(expected_result, passingcars.passingcars(A))


class TestDNA(unittest.TestCase):
    """Test genomic range query"""

    def test_1(self):
        S = 'CAGCCTA'
        P = [2, 5, 0]
        Q = [4, 5, 6]
        expected_result = [2, 4, 1]

        self.assertEqual(expected_result, DNA.genomic_range_query(S,P,Q))



if '__name__' == '__main__':
    unittest.main()
