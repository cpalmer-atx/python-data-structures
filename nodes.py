# File: nodes.py
# Author: Chad Palmer
# Date: May 2020
# Description:
#       This file creates Nodes for many types of common data structures
#       beginning with a Node class.  Child classes inherit Node and add
#       the required functionality for its respective application.

# Parent Class
class Node:
    def __init__(self, data=None):
        self.data = data

    def __str__(self):
        return str(self.data)


# Child classes inherit from Node class.

class ListNode(Node):
    def __init__(self, data=None):
        super().__init__(data)
        self.next = None


class DoublyListNode(Node):
    def __init__(self, data=None):
        super().__init__(data)
        self.prev = None
        self.next = None


class BSTNode(Node):
    def __init__(self, data=None):
        super().__init__(data)
        self.left_child = None
        self.right_child = None
