# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            tmp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(tmp)
            return root
        return None


node_one = TreeNode(1)

node_two = TreeNode(2)
node_three = TreeNode(3)

node_one.left = node_two

node_two.left = node_three

s = Solution()
print s.invertTree(node_one)
