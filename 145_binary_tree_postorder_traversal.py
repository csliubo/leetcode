# -*- coding:utf-8 -*-
from typing import List

from utils import TreeNode

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        params = []

        ret = []
        params.append(root)
        visited = set()
        while params:
            current_node = params[-1]

            if current_node in visited:
                ret.append(current_node.val)
                params.pop()
                continue

            visited.add(current_node)
            if current_node.right:
                params.append(current_node.right)
            if current_node.left:
                params.append(current_node.left)

        return ret
