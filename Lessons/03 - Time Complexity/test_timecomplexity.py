import unittest
import frgjmp


class TestFRGJMP(unittest.TestCase):
    """Test FRGJMP Challenge."""

    def test_1(self):
        """Proposed test 1."""
        X = 10
        Y = 85
        D = 30

        # after the third jump, the frog would have reached Y and beyond
        expected_result = 3
        self.assertEqual(frgjmp.frogjump(X=X, Y=Y, D=D), expected_result)

    def own_test_1(self):
        """Own test 1."""
        X = 20
        Y = 100
        D = 12
        expected_result = 4

        self.assertEqual(frgjmp.frogjump(X=X, Y=Y, D=D), expected_result)


class TestPermMissingElem(unittest.TestCase):
    """Test permMissingElem Challenge."""

    pass


class TestTapeEquilibrium(unittest.TestCase):
    """Test tapeEquilibrium Challenge."""

    pass


if __name__ == '__main__':
    unittest.main()
