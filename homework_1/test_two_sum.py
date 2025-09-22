from .two_sum import two_sum
import unittest


class TestIndexSearcher(unittest.TestCase):
    def test_1(self):
        """
        Тест из moodle
        """

        self.assertEqual(two_sum([2, 7, 11, 15], 9), (0, 1))

    def test_2(self):
        """
        Тест из moodle
        """

        self.assertEqual(two_sum([3, 2, 4], 6), (1, 2))

    def test_3(self):
        """
        Тест из moodle
        """

        self.assertEqual(two_sum([3, 3], 6), (0, 1))

    def test_4(self):
        """
        Тест на вход пустого массива
        """

        self.assertEqual(two_sum([], 6), None)

    def test_5(self):
        """
        Тест на неправильную сумму
        """

        self.assertEqual(two_sum([4, 5], 6), None)

    def test_6(self):
        """
        Тест на дробные числа
        """

        self.assertEqual(two_sum([3, 3.0], 6), (0, 1))

    def test_7(self):
        """
        Тест на целочислленный строковый ввод
        """
        self.assertEqual(two_sum([3, '3.0'], 6), (0, 1))

    def test_8(self):
        """
        Тест на некоректный строковый ввод
        """

        self.assertEqual(two_sum([3, "tree"], 6), None)

    def test_9(self):
        """
        Тест на пустую сумму
        """

        self.assertEqual(two_sum([3, None], 6), None)

    def test_10(self):
        """
        Тест на целочислленный строковый ввод
        """
        self.assertEqual(two_sum([3, '-3.0'], 0), (0, 1))

    def test_11(self):
        """
        Тест на целочислленный строковый ввод
        """
        self.assertEqual(two_sum([3, '3.1'], 6), None)

    def test_12(self):
        """
        Тест на целочислленный строковый ввод
        """
        self.assertEqual(two_sum([3, '-4'], -1), (0, 1))


if __name__ == '__main__':
    unittest.main(verbosity=2)
