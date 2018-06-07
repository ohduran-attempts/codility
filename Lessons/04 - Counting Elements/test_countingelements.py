import unittest
import frogRiverOne
import maxCounters
import missingInteger


class TestFrogRiverOne(unittest.TestCase):
    """Test frogRiverOne."""

    def test_1(self):
        """Proposed test 1."""
        A = [1, 3, 1, 4, 2, 3, 5, 4]
        X = 5
        expected_result = 6  # the index where all leaves are set

        self.assertEqual(frogRiverOne.frogriverone(A, X), expected_result)

    def own_test_1(self):
        """Own test 1."""
        A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        X = 2
        expected_result = -1
        self.assertEqual(frogRiverOne.frogriverone(A, X), expected_result)


class TestMaxCounters(unittest.TestCase):
        """Test Max Counters challenge."""

        def test_1(self):
                """Proposed test 1."""
                A = [3, 4, 4, 6, 1, 4, 4]
                N = 5
                expected_result = [3, 2, 2, 4, 2]

                self.assertEqual(maxCounters.maxcounters(N,A), expected_result)

        def own_test_2(self):
                """Own test 2."""
                N = 1
                A = [1, 2, 1, 2]
                expected_result = [2]

                self.assertEqual(maxCounters.maxcounters(N,A), expected_result)


class TestMissingInteger(unittest.TestCase):
        """Test Missing Integer challenge."""

        def test_1(self):
                """Proposed test 1."""
                A = [1, 2, 3]
                expected_result = 4

                self.assertEqual(
                        missingInteger.missinginteger(A), expected_result)

        def test_2(self):
                """Proposed test 2."""
                A = [1, 3, 6, 4, 1, 2]
                expected_result = 5

                self.assertEqual(
                        missingInteger.missinginteger(A), expected_result)

        def test_3(self):
                """Proposed test 3."""
                A = [-1, -3]
                expected_result = 1

                self.assertEqual(
                        missingInteger.missinginteger(A), expected_result)


if __name__ == '__main__':
    unittest.main()
