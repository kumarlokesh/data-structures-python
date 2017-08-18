"""
Added an implementation of Binary Search Tree.
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, start, value):
        if value > start.value:
            if start.right:
                self.insert_helper(start.right, value)
            else:
                start.right = Node(value)
        else:
            if start.left:
                self.insert_helper(start.left, value)
            else:
                start.left = Node(value)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, start, value):
        if start:
            if value == start.value:
                return True
            elif value > start.value:
                return self.search_helper(start.right, value)
            else:
                return self.search_helper(start.left, value)
        return False
