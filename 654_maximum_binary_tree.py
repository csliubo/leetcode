# -*- coding:utf-8 -*-
from utils import drawtree

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
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        max_pos = 0
        max = nums[0]
        for i in range(1, nums.__len__()):
            if nums[i] > max:
                max_pos = i
                max = nums[i]
        node = TreeNode(max)
        node.left = self.constructMaximumBinaryTree(nums[:max_pos])
        node.right = self.constructMaximumBinaryTree(nums[max_pos + 1:])
        return node


lst = [3, 2, 1, 6, 0, 5]
s = Solution()
tree = s.constructMaximumBinaryTree(lst)
drawtree(tree)
