import unittest
from homework_3 import gen_bin_tree, gen_bin_tree_preorder_list


class TestFunctionsTask(unittest.TestCase):

    def test_gen_bin_tree_node(self):
        """
        Тестирование бинарного дерева, хранящегося с использованием объектов
        """
        example_tree = {
            "value": 9,
            "left": {
                "value": 19,
                "left": { "value": 39, "left": None, "right": None },
                "right": { "value": 37, "left": None, "right": None }
            },
            "right": {
                "value": 17,
                "left": { "value": 35, "left": None, "right": None },
                "right": { "value": 33, "left": None, "right": None }
            },
        }
        self.assertEqual(
            gen_bin_tree(3, 9, lambda x: 2*x + 1, lambda x: 2*x - 1).to_json(),
            example_tree
        )
        with self.assertRaises(ValueError):
            self.assertEqual(
                gen_bin_tree(-1, 9, lambda x: 2*x + 1, lambda x: 2*x - 1).to_json(),
                example_tree
            )

    def test_gen_bin_tree_preorder(self):
        """
        Тестирование бинарного дерева, хранящегося в прямом порядке
        :return:
        """
        example_tree = [9, 19, 39, 37, 17, 35, 33]
        self.assertEqual(
            gen_bin_tree_preorder_list(3, 9, lambda x: 2 * x + 1, lambda x: 2 * x - 1),
            example_tree
        )
        with self.assertRaises(ValueError):
            self.assertEqual(
                gen_bin_tree_preorder_list(-1, 9, lambda x: 2 * x + 1, lambda x: 2 * x - 1),
                example_tree
            )


if __name__ == '__main__':
    unittest.main(verbosity=2)
