"""
An implementation of Linked List is provided below.
Following methods are provided for carrying out operations on LinkedList:
- "append" adds new node at the end of the list.
- "get_node" returns node at a certain position.
- "insert" will add a node to a particular position in the list.
   e.g. Inserting node at position 3 means inserting node between
   position 2 and 3.
- "delete" will delete the first node having matching value as that
   of the supplied value.

Note: Positions in Linked List start from 1.
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        """
        self.next is placeholder for reference to next node
        in the LinkedList.
        """


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, node):
        current = self.head
        if self.head:
            while current.next:
                """
                Iterate through LinkedList till we reach
                end of the list.
                """
                current = current.next
            current.next = node
        else:
            """
            If LinkedList is empty, i.e. head is not present
            then assign node at head position
            """
            self.head = node

    def get_node(self, position):
        if not self.head or (position < 1):
            return None
        if position == 1:
            return self.head
        counter = 1
        current = self.head
        while current.next:
            current = current.next
            counter += 1
            if counter == position:
                return current

        return None

    def insert(self, node, position):
        if position < 1:
            return False
        if position == 1:
            node.next = self.head
            self.head = node
            return True
        counter = 1
        current = self.head
        while current.next:
            if counter == (position -  1):
                node.next = current.next
                current.next = node
                return True
            current = current.next
            counter += 1

        return False

    def delete(self, value):
        if not self.head:
            return False
        if self.head.value == value:
            self.head = self.head.next
            return True
        previous = current = self.head
        while current.next:
            current = current.next
            if current.value == value:
                previous.next = current.next
                return True
            previous = current
        return False
