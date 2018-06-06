import unittest
import frogRiverOne


class TestFrogRiverOne(unittest.TestCase):
    """Test frogRiverOne."""

    def test_1(self):
        """Proposed test 1."""
        A = [1, 3, 1, 4, 2, 3, 5, 4]
        X = 5
        expected_result = 6  # the index where all leaves are set

        self.assertEqual(frogRiverOne.frogriverone(A, X), expected_result)



if __name__ == '__main__':
    unittest.main()
