import unittest

from lanka_data_mind import run_lanka_data_mind


class TestCase(unittest.TestCase):

    def test_dump(self):
        self.assertTrue(run_lanka_data_mind._run())


if __name__ == '__main__':
    unittest.main()
