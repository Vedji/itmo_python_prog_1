from typing import Callable
from homework_3 import Node


def gen_bin_tree(height: int, root: int, left: Callable[[int], int], right: Callable[[int], int]) -> Node:
    """
    Рекурсивно строит бинарное дерево заданной высоты, используя объекты

    Args:
        height: Высота дерева
        root: Значение корневого узла
        left: Функция для вычисления значения левого потомка
        right: Функция для вычисления значения правого потомка

    Returns:
        Корневой узел бинарного дерева

    Raises:
        ValueError: Если высота меньше или равна 0
    """
    if height <= 0:
        raise ValueError("Высота дерева не может быть отрицательной")
    if height == 1:
        return Node(root)
    return Node(
        root,
        gen_bin_tree(height - 1, left(root), left, right),
        gen_bin_tree(height - 1, right(root), left, right)
    )


def gen_bin_tree_preorder_list(
        height: int,
        root: int,
        left: Callable[[int], int],
        right: Callable[[int], int]
) -> list[int]:
    """
    Рекурсивно строит бинарное дерево заданной высоты, используя прямой порядок

    Args:
        height: Высота дерева
        root: Значение корневого узла
        left: Функция для вычисления значения левого потомка
        right: Функция для вычисления значения правого потомка

    Returns:
        Список значений узлов в прямом порядке

    Raises:
        ValueError: Если высота меньше или равна 0
    """
    if height <= 0:
        raise ValueError("Высота дерева не может быть отрицательной")
    if height == 1:
        return [root]
    return [
        root,
        *gen_bin_tree_preorder_list(height - 1, left(root), left, right),
        *gen_bin_tree_preorder_list(height - 1, right(root), left, right)
    ]
