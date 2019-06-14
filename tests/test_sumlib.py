# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

# If you want to pass without testing modules uncomment this function, and comment rest of the script
# def test_success():
#     assert True


import unittest
import sumlib

class Test_sumlib(unittest.TestCase):

    # Returns True or False.
    def test(self):
        self.assertTrue(True)

    # Returns True or False.
    def test_dosum(self):
        num_sum = sumlib.dosum(10, 20)
        expected_sum = 30

        self.assertTrue(num_sum, expected_sum)

    # Returns True or False.
    def test_domatrixsum(self):
        mat_sum = sumlib.domatrixsum([10, 20], [3, 4])
        expected_sum = [13, 24]
        self.assertTrue(mat_sum, expected_sum)


if __name__ == '__main__':
    unittest.main()