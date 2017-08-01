"""
An implementation of Stack based on LinkedList is provided below.
Following methods are provided for carrying out operations on Stack:
- "push" add a node onto the top of stack.
- "pop" remove a node from the top of the stack.
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_first(self, node):
        if not self.head:
            self.head = node
            return True
        node.next = self.head
        self.head = node
        return True

    def delete_first(self):
        if not self.head:
            return None
        current = self.head
        self.head = self.head.next
        current.next = None
        return current


class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, node):
        self.ll.insert_first(node)

    def pop(self):
        return self.ll.delete_first()
