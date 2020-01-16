# -*- coding:utf-8 -*-
import cProfile
import time

from utils import deserialize, drawtree

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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes = []
        childs = []
        if not root:
            return True
        nodes.append(root)
        while nodes.__len__() != 0:
            need_continue = False
            for node in nodes:
                if not node:
                    childs.append(None)
                    childs.append(None)

                else:
                    childs.append(node.left)
                    childs.append(node.right)
            # 检查childs是否对称
            childs_len = childs.__len__()
            new_left_nodes = []
            new_right_nodes = []
            for i in range(0, childs.__len__() / 2):
                left = childs[i]
                right = childs[childs_len - i - 1]
                if not left and not right:
                    continue
                if left and right and left.val == right.val:
                    new_left_nodes.append(left)
                    new_right_nodes.insert(0, right)
                    continue
                return False
            if new_left_nodes and new_right_nodes:
                # 对nodes进行收缩
                # print new_left_nodes, new_right_nodes
                # print new_left_nodes.reverse(), new_right_nodes.reverse()
                new_left_nodes.extend(new_right_nodes)
                nodes = new_left_nodes
                childs = []
            else:
                return True
        return True


root = deserialize('[1,2,2,3,4,4,3]')
s = Solution()
# print s.isSymmetric(root)
root = deserialize(
    '[6,82,82,null,53,53,null,-58,null,null,-58,null,-85,-85,null,-9,null,null,-9,null,48,48,null,33,null,null,33,81,null,null,81,5,null,null,5,61,null,null,61,null,9,9,null,91,null,null,91,72,7,7,72,89,null,94,null,null,94,null,89,-27,null,-30,36,36,-30,null,-27,50,36,null,-80,34,null,null,34,-80,null,36,50,18,null,null,91,77,null,null,95,95,null,null,77,91,null,null,18,-19,65,null,94,null,-53,null,-29,-29,null,-53,null,94,null,65,-19,-62,-15,-35,null,null,-19,43,null,-21,null,null,-21,null,43,-19,null,null,-35,-15,-62,86,null,null,-70,null,19,null,55,-79,null,null,-96,-96,null,null,-79,55,null,19,null,-70,null,null,86,49,null,25,null,-19,null,null,8,30,null,82,-47,-47,82,null,30,8,null,null,-19,null,25,null,49]')
print time.time()
print s.isSymmetric(root)
print time.time()
# drawtree(root)
