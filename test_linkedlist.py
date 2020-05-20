# File: test_linkedlist.py
# Author: Chad Palmer
# Date: May 2020
# Description:
#       This file tests the LinkedList class with Test Driven Development
#       in mind.  Linked lists are retrieved as a python list for easy
#       value comparisions.  The __str__ dunder method in the Node class
#       makes it possible to run these test cases against classes with
#       any primative data type stored in the list.

import unittest
import numpy as np
from linkedlist import LinkedList


class TestLinkedList(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.appendList = LinkedList()

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
