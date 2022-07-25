import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(1, 3), 4)

    def test_divide(self):
        self.assertEqual(calc.divide(3, 2), 1.5)

        self.assertRaises(ValueError, calc.divide, 11, 0)
        #Or
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
