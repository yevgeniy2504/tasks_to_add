# Необходимо превратить собранное на семинаре дерево поиска в полноценное левостороннее красно-черное дерево.
# И реализовать в нем метод добавления новых элементов с балансировкой.
#
# Красно-черное дерево имеет следующие критерии:
# • Каждая нода имеет цвет (красный или черный)
# • Корень дерева всегда черный
# • Новая нода всегда красная
# • Красные ноды могут быть только левым ребенком
# • У краной ноды все дети черного цвета
#
# Соответственно, чтобы данные условия выполнялись, после добавления элемента в дерево необходимо произвести
# балансировку, благодаря которой все критерии выше станут валидными. Для балансировки существует
# 3 операции – левый малый поворот, правый малый поворот и смена цвета.

class Node:
    def __init__(self, key, parent=None, color='red'):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color


class RedBlackTree:
    def __init__(self):
        self.root = None

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.key, node.color)
            self.inorder_traversal(node.right)

    def print_tree(self):
        self.inorder_traversal(self.root)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            self.root.color = 'black'
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, node)
                self.balance(node.left)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key, node)
                self.balance(node.right)
            else:
                self._insert(node.right, key)

    def balance(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)

        self.root.color = 'black'

    def left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child


if __name__ == "__main__":
    tree = RedBlackTree()
    keys = [10, 20, 30, 15, 25, 28, 27, 5]
    for key in keys:
        tree.insert(key)

    tree.print_tree()
