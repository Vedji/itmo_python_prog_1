from typing import Optional


class Node:

    def __init__(self, value: int, left: Optional["Node"] = None, right: Optional["Node"] = None):
        """
        Узел бинарного дерева

        Attributes:
            value: Значение узла
            left: Левый лист
            right: Правый лист
        """
        self.value = value
        self.left = left
        self.right = right

    def to_json(self) -> dict[str, Optional["Node"]]:
        """
        Преобразует бинарное дерево в json-формат

        Returns:
            Словарь с бинарным деревом, с ключами: 'value', 'left', 'right'
        """
        return {
            "value": self.value,
            "left": self.left.to_json() if self.left else None,
            "right": self.right.to_json() if self.right else None
        }
