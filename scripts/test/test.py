import unittest


class Test(unittest.TestCase):
    '''
    Main Test class
    Excecuting this file will run all the tests in this class
    '''
    def test(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    # Unit Test main module
    unittest.main()
