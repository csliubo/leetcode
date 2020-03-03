# -*- coding:utf-8 -*-
from utils import deserialize, TreeNode

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def levelOrder(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if not root:
            return ret
        # ret.append(root.val)
        travel_nodes = [root]
        while travel_nodes:
            new_nodes = []
            travel_vals = []
            for node in travel_nodes:
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
                travel_vals.append(node.val)
            ret.append(travel_vals)
            travel_nodes = new_nodes
        return ret


root = deserialize('[1,2,2,3,4,4,3]')
s = Solution()
r = s.levelOrder(root)
root = deserialize('[3,9,20,null,null,15,7]')
r = s.levelOrder(root)
print(r)
