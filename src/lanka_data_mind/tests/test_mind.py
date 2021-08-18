import unittest

from lanka_data_mind import mind


class TestCase(unittest.TestCase):

    def test_dump(self):
        self.assertTrue(mind._run())


if __name__ == '__main__':
    unittest.main()
