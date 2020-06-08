# File: test_linkedlist.py
# Author: Chad Palmer
# Date: May 2020
# Description:
#       This file tests the LinkedList class with Test Driven Development
#       in mind.  Linked lists are retrieved as a python list for easy
#       value comparisions.  The __str__ dunder method in the Node class
#       makes it possible to run these test cases against classes with
#       any primative data type stored in the list.  For future improvement,
#       tests should be isolated ( count() is a perfect example of this).

import unittest
import numpy as np
from linkedlist import LinkedList


class TestLinkedList(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.appendList = LinkedList()
        self.countList = LinkedList()

    @classmethod
    def tearDown(self):
        pass

    def test_append(self):

        self.appendList.append(5)
        self.appendList.append('a')
        self.appendList.append(5.5)
        self.appendList.append(-3)
        self.appendList.append('test string')

        arrayList = np.array(self.appendList.getList())
        cnt = self.appendList.count()

        self.assertEqual(arrayList[cnt - 5], '5')
        self.assertEqual(arrayList[cnt - 4], 'a')
        self.assertEqual(arrayList[cnt - 3], '5.5')
        self.assertEqual(arrayList[cnt - 2], '-3')
        self.assertEqual(arrayList[cnt - 1], 'test string')

    def test_count(self):

        self.countList.push(1)
        self.countList.push(2)
        self.countList.append(3)
        self.countList.append(4)
        self.countList.pop()

        self.assertEqual(self.countList.count(), 3)


if __name__ == '__main__':
    unittest.main()
