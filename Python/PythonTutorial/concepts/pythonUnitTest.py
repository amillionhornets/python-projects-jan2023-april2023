import functionTests
import unittest

class TestMultiply(unittest.TestCase):
    def test_with_two_positives(self):
        self.assertEqual(functionTests.multiplyWithLoop(17,19), 17 * 19)
        self.assertEqual(functionTests.multiplyWithLoop(1389173,139871313), 1389173 * 139871313)
        self.assertEqual(functionTests.multiplyWithLoop(1,2), 2)

    def test_with_one_zero(self):
        self.assertEqual(functionTests.multiplyWithLoop(17,0), 0)
        self.assertEqual(functionTests.multiplyWithLoop(0, 17), 0)

    def test_with_two_zero(self):
        self.assertEqual(functionTests.multiplyWithLoop(0,0), 0)

    def test_with_one_negative(self):
        self.assertEqual(functionTests.multiplyWithLoop(17,-19), 17 * -19)
        self.assertEqual(functionTests.multiplyWithLoop(-19, 17), -19 * 17)

    def test_with_two_negative(self):
        self.assertEqual(functionTests.multiplyWithLoop(-17,-19), 17 * 19)
        self.assertEqual(functionTests.multiplyWithLoop(-19, -17), 19 * 17)

# To run must go into folder in cmd and run with python -m unittest pythonUnitTest.py
unittest.main()