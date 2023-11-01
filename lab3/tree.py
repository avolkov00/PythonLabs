class TreeNode:
    """ Нода дерева"""

    def __init__(self, key=None):
        """Конструктор ноды"""
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if self.key is None:
            self.key = key
            return

        if key < self.key:
            if self.left is None:
                self.left = TreeNode(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = TreeNode(key)
            else:
                self.right.insert(key)
        else:
            raise ValueError(f"Key {key} already exists")

    def __str__(self):
        """Строковое представление ноды"""
        return f"TreeNode({self.key})"

    def tree_traversal(self, node):
        """Генератор для прохода по всей ноде"""
        if node is None:
            pass

        if node.left is not None:
            yield from self.tree_traversal(node.left)

        yield node.key

        if node.right is not None:
            yield from self.tree_traversal(node.right)

    def __iter__(self):
        yield from self.tree_traversal(self)


tree = TreeNode()
tree.insert(9)
tree.insert(17)
tree.insert(4)
tree.insert(3)
tree.insert(6)
tree.insert(5)

for i in tree:
    print(i)
