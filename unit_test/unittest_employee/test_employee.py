import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    '''
    setUpClass and tearDownClass are run once for the whole class; setUp and tearDown are run before and after each test method
    '''

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.assertEqual(self.emp_1.pay, 100000)

if __name__ == '__main__':
    unittest.main()