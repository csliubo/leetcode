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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        head = None
        last_node = None
        while l1 and l2:
            if l1.val <= l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            if last_node:
                last_node.next = node
            last_node = node
            if not head:
                head = node
            if not l1:
                last_node.next = l2
            elif not l2:
                last_node.next = l1
        return head


def print_lst(root):
    while root:
        print root.val
        root = root.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(8)
l1.next.next.next = ListNode(10)

l2 = ListNode(4)
l2.next = ListNode(5)
l2.next.next = ListNode(11)

# print_lst(l1)
# print_lst(l2)

# l1 = []
l2=None

s = Solution()
print_lst(s.mergeTwoLists(l1, l2))
