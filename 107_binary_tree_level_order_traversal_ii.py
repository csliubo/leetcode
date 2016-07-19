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
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        current_level_queue = []
        current_level_queue.append(root)
        ret = []
        while current_level_queue and current_level_queue.__len__() > 0:
            lst = []
            next_level_queue = []
            for node in current_level_queue:
                lst.append(node.val)
                if node.left:
                    next_level_queue.append(node.left)
                if node.right:
                    next_level_queue.append(node.right)
            if lst:
                ret.append(lst)
            current_level_queue = next_level_queue
        return ret[::-1]


# [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
print s.levelOrderBottom(root)
