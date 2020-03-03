# -*- coding:utf-8 -*-
from typing import List

from utils import TreeNode

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        params = []

        ret = []
        params.append(root)
        visited = set()
        while params:
            current_node = params[-1]

            if current_node in visited:
                params.pop()
                continue
            visited.add(current_node)
            ret.append(current_node.val)
            if current_node.right:
                params.append(current_node.right)
            if current_node.left:
                params.append(current_node.left)

        return ret
