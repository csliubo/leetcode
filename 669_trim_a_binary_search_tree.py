# -*- coding:utf-8 -*-
from utils import TreeNode, drawtree

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val < L:
            return self.trimBST(root.right, L, R)
        elif root.val <= R:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root
        else:
            return self.trimBST(root.left, L, R)


root = TreeNode(3)
root.left = TreeNode(2)
root.left.left = TreeNode(1)

root.right = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(6)
root.right.right.right = TreeNode(9)
s = Solution()
drawtree(s.trimBST(root, 2, 6))
# drawtree(root)
