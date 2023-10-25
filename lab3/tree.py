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

    def print_hierarchy(self, dir="root", level=0):
        """Печать всей иерархии ноды"""
        print(f"[{dir}] #{level} = {self.key} | left = {self.left} | right = {self.right}")
        if self.left is not None: self.left.print_hierarchy("left", level + 1)
        if self.right is not None: self.right.print_hierarchy("right", level + 1)

    def preorder_print(self, node):
        """Генератор для прохода по всей ноде"""
        if node is None:
            pass

        if node.left is not None:
            yield from self.preorder_print(node.left)

        yield node.key

        if node.right is not None:
            yield from self.preorder_print(node.right)

    def postorder_print(self):
        """Генератор для прохода по дереву с текущим элементом в качестве корня"""
        if self.key is None:
            pass

        if self.left is not None:
            yield from self.preorder_print(self.left)

        yield self.key

        if self.right is not None:
            yield from self.preorder_print(self.right)

    def __iter__(self):
        yield from self.postorder_print()


tree = TreeNode()
tree.insert(9)
tree.insert(17)
tree.insert(4)
tree.insert(3)
tree.insert(6)
tree.insert(5)
# tree.print_hierarchy()
# tree.postorder_print()

for i in tree:
    print(i)
# tree.insert(3) # exception
