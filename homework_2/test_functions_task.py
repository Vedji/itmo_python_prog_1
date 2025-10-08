import unittest
from homework_2 import guess_number, SearchType


class TestFunctionsTask(unittest.TestCase):

    def test_from_lessons(self):
        list_from_example = [1, 3, 5, 7, 11, 13, 17, 19, 23, 19, 31, 37, 41, 43, 47, 53, 59]
        self.assertEqual(guess_number(37, list_from_example, SearchType.BINARY_SEARCH), (37, 3))
        self.assertEqual(guess_number(37, list_from_example, SearchType.SLOW_SEARCH), (37, 11))


if __name__ == '__main__':
    unittest.main(verbosity=2)
