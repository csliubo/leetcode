# -*- coding:utf-8 -*-
from typing import List

from utils import TreeNode

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        params = []

        ret = []
        params.append(root)
        visited = set()
        while params:
            current_node = params[-1]
            if isinstance(current_node, int):
                ret.append(current_node)
                params.pop()
                continue
            if current_node in visited:
                params.pop()
                continue
            visited.add(current_node)

            if current_node.right:
                params.append(current_node.right)
            params.append(current_node.val)
            if current_node.left:
                params.append(current_node.left)

        return ret
