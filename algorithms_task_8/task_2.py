"""
Задание 2.

Доработайте пример структуры "дерево", рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения

Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде.
"""


class BinaryTreeNode:
    def __init__(self, value):
        if value is None:
            raise ValueError("Значение узла не может быть пустым")
        self.value = value
        self.left_child = None  # Левый потомок
        self.right_child = None  # Правый потомок


class BinaryTree:
    def __init__(self, root_obj):
        if root_obj is None:
            raise ValueError("Значение корня не может быть пустым")
        self.root = BinaryTreeNode(root_obj)  # Установка корня дерева

    def insert_left(self, parent_node, new_node):
        if parent_node is None or new_node is None:
            raise ValueError("Родительский узел и новый узел не могут быть пустыми")
        if not isinstance(parent_node, BinaryTreeNode):
            raise ValueError("Родительский узел должен быть экземпляром BinaryTreeNode")
        parent_node.left_child = BinaryTreeNode(new_node)  # Вставка левого потомка

    def insert_right(self, parent_node, new_node):
        if parent_node is None or new_node is None:
            raise ValueError("Родительский узел и новый узел не могут быть пустыми")
        if not isinstance(parent_node, BinaryTreeNode):
            raise ValueError("Родительский узел должен быть экземпляром BinaryTreeNode")
        parent_node.right_child = BinaryTreeNode(new_node)  # Вставка правого потомка

    def get_right_child(self, parent_node):
        if parent_node is None:
            raise ValueError("Родительский узел не может быть пустым")
        if not isinstance(parent_node, BinaryTreeNode):
            raise ValueError("Родительский узел должен быть экземпляром BinaryTreeNode")
        return parent_node.right_child  # Получение правого потомка

    def get_left_child(self, parent_node):
        if parent_node is None:
            raise ValueError("Родительский узел не может быть пустым")
        if not isinstance(parent_node, BinaryTreeNode):
            raise ValueError("Родительский узел должен быть экземпляром BinaryTreeNode")
        return parent_node.left_child  # Получение левого потомка

    def set_root_val(self, value):
        if value is None:
            raise ValueError("Значение корня не может быть пустым")
        self.root = BinaryTreeNode(value)  # Установка значения корня

    def get_root_val(self):
        return self.root.value  # Получение значения корня


# Пример использования
if __name__ == "__main__":
    try:
        r = BinaryTree(8)
        print(r.get_root_val())
        r.insert_left(r.root, 40)
        print(r.get_left_child(r.root).value)
        r.insert_right(r.root, 12)
        print(r.get_right_child(r.root).value)
    except ValueError as e:
        print(f"Ошибка: {e}")

