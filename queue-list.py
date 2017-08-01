"""
An implementation of Queue using Python list data structure.
Following methods are provided to carry out operations on Queue:
- "enqueue" adds node to tail position.
- "dequeue" removes node from head position.
- "peek" provides value of node at head position.
"""

class Queue(object):
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, node):
        self.storage.append(node)

    def peek(self):
        if self.storage:
            return self.storage[0]
        return None

    def dequeue(self):
        if self.storage:
            return self.storage.pop(0)
        return None
