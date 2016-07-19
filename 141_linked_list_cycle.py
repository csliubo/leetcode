# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 快慢指针,如果相遇则说明有环
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow_node = head
        fast_node = head
        while slow_node and fast_node:

            slow_node = slow_node.next
            fast_node = fast_node.next
            if not fast_node:
                return False
            fast_node = fast_node.next
            if slow_node == fast_node:
                return True
        return False
