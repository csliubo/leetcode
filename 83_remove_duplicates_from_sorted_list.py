# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last_node = None
        node = head
        while node:
            if last_node and last_node.val == node.val:
                last_node.next = node.next
            else:
                last_node = node
            node = node.next
        return head
