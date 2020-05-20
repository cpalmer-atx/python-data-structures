from nodes import ListNode as Node


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while (cur.next != None):
            cur = cur.next
        cur.next = new_node
        self.length += 1

    def display(self):
        elements = []
        cur = self.head
        while (cur.next != None):
            cur = cur.next
            elements.append(cur.data)
        print(elements)

    def getList(self):
        elements = []
        cur = self.head
        while (cur.next != None):
            cur = cur.next
            elements.append(cur.data)
        return elements

    def count(self):
        return self.length


# test = LinkedList()
# test.display()
# test.append(1)
# test.append(2)
# test.append(3)
# test.display()
