'''
test file
'''

import unittest
import my_cap

class TestCap(unittest.TestCase):

    '''
    test class
    '''
    def test_my_cap(self):

        '''
        test method
        '''
        self.assertEqual(my_cap.cap_text('python'), 'Python')


if __name__=='__main__':
    unittest.main()
