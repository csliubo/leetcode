# -*- coding:utf-8 -*-
from utils import deserialize

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
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root:
            if root.left and root.right:
                return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
            elif root.left or root.right:
                if root.left:
                    return 1 + self.minDepth(root.left)
                if root.right:
                    return 1 + self.minDepth(root.right)
            else:
                return 1
        return 0


root = deserialize('[1,2,2,3,4,4,3]')
s = Solution()
r = s.minDepth(root)
print(r)
root = deserialize('[3,9,20,null,null,15,7]')
r = s.minDepth(root)
print(r)
root = deserialize('[3,9]')
r = s.minDepth(root)
print(r)
