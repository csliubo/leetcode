# -*- coding:utf-8 -*-
from utils import deserialize, drawtree

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left_balanced, left_depth = self.get_depth(root.left)
        right_balanced, right_depth = self.get_depth(root.right)
        if not left_balanced or not right_balanced:
            return False
        return abs(left_depth - right_depth) <= 1

    def get_depth(self, root):
        if not root:
            return True, 0
        if not root.left and not root.right:
            return True, 1
        left_balanced, left_depth = self.get_depth(root.left)
        if not left_balanced:
            return False, 0
        right_balanced, right_depth = self.get_depth(root.right)
        if not right_balanced:
            return False, 0
        if abs(left_depth - right_depth) <= 1:
            return True, 1 + max(left_depth, right_depth)
        return False, 0


root = deserialize('[1,2,3,4,5,6,7,8,9,10,11,12,13,null,null,15,16]')

s = Solution()
print s.isBalanced(root)
drawtree(root)
