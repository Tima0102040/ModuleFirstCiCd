import unittest
from numLines import numLines
from numWords import numWords

class TestNumLinesAndWords(unittest.TestCase):

    def test_num_lines(self):
        num_lines = 0
        fname = 'test_file.txt'
        with open(fname, 'w') as f:
            f.write(
                "Hello world. This is a test. Second line of the test. Third line of the test. Fourth line of the test.")

        with open(fname, 'r') as f:
            content = f.read()
            self.assertEqual(content.count('.'), numLines(num_lines, fname))

    def test_num_words(self):
        num_words = 0
        fname = 'test_file.txt'
        with open(fname, 'w') as f:
            f.write(
                "Hello world. This is a test. Second line of the test. Third line of the test. Fourth line of the test.")

        with open(fname, 'r') as f:
            content = f.read()
            self.assertEqual(len(content.split()), numWords(num_words, fname))


if __name__ == '__main__':
    unittest.main()