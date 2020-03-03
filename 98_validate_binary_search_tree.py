# -*- coding:utf-8 -*-
from utils import TreeNode, deserialize, drawtree

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def isValidBST1(self, root: TreeNode) -> bool:
        if not root:
            return True

        def valid(root: TreeNode, near_min=None, near_max=None) -> bool:
            if not root:
                return True
            if root.left:
                if root.left.val >= root.val:
                    return False
                elif near_min and root.left.val <= near_min:
                    return False
            if root.right:
                if root.right.val <= root.val:
                    return False
                elif near_max and root.right.val >= near_max:
                    return False
            if root.left and root.right:
                return valid(root.left, near_max=root.val, near_min=near_min) and valid(root.right, near_min=root.val,
                                                                                        near_max=near_max)
            elif root.left:
                return valid(root.left, near_max=root.val, near_min=near_min)
            elif root.right:
                return valid(root.right, near_min=root.val, near_max=near_max)
            else:
                return True

        return valid(root)

    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node: TreeNode, near_min=None, near_max=None):
            if not node:
                return True
            if near_min is not None and node.val <= near_min:
                return False
            if near_max is not None and node.val >= near_max:
                return False
            return valid(node.left, near_min=near_min, near_max=node.val) and valid(node.right, near_min=node.val,
                                                                                    near_max=near_max)

        return valid(root)


if __name__ == "__main__":
    s = Solution()
    root = deserialize("[0,null,-1]")
    # drawtree(root)
    ret = s.isValidBST(root)
    print(ret)
