"""
Added an implementation of HashTable with string keys.
Keys are calculated using the first two letters of the string.
Uppercase strings having atleast 2 characters are expected.
"""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hash_value = self.calculate_hash_value(string)
        if not self.is_valid_hash_value(hash_value):
            return
        if self.table[hash_value] is None:
            self.table[hash_value] = [string]
        else:
            self.table[hash_value].append(string)

    def lookup(self, string):
        hash_value = self.calculate_hash_value(string)
        if self.is_valid_hash_value(hash_value) and self.table[hash_value] and (string in self.table[hash_value]):
            return hash_value
        return -1

    def calculate_hash_value(self, string):
        if len(string) < 2:
            return -1
        return ord(string[0]) * 100 + ord(string[1])

    def is_valid_hash_value(self, value):
        return value > -1 and value < len(self.table)
