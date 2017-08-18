"""
Added an implementation of BinaryTree.
Added pre-order depth first search function.
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return self.preorder_search(self.root, find_val)

    def traverse_tree(self):
        return "-".join(self.preorder_traverse(self.root, []))

    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_traverse(self, start, traversal):
        if start:
            traversal.append(str(start.value))
            traversal = self.preorder_traverse(start.left, traversal)
            traversal = self.preorder_traverse(start.right, traversal)
        return traversal
