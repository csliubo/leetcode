# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        if not head:
            return None
        lst = list()
        while head.next:
            print head.val
            lst.append(head.val)
            head = head.next
        lst.append(head.val)
        return self.genBst(lst)

    def genBst(self, lst):
        if not lst:
            return None
        len = lst.__len__()
        if len == 1:
            return TreeNode(lst[0])
        else:
            middle = len / 2
            node = TreeNode(lst[middle])
            node.left = self.genBst(lst[:middle])
            node.right = self.genBst(lst[middle + 1:])
            return node


def print_bst(node):
    tmp = node
    # print node.left.val, node.right.val
    if tmp.left:
        print_bst(tmp.left)
    print tmp.val
    if tmp.right:
        print_bst(tmp.right)


head = ListNode(1)
temp = head
for i in range(2, 100):
    node = ListNode(i)
    temp.next = node
    temp = node

s = Solution()
bst = s.sortedListToBST(head)
print_bst(bst)

