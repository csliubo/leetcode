from typing import List

from utils import TreeNode, deserialize, drawtree

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def maxProduct(self, root: TreeNode) -> int:

        left_sum = {}
        right_sum = {}

        def travel(node: TreeNode):
            left_count, right_count = 0, 0
            if node.left:
                left_count = travel(node.left)
                left_sum[node] = left_count
            if node.right:
                right_count = travel(node.right)
                right_sum[node] = right_count
            return node.val + left_count + right_count

        total_sum = travel(root)

        self.global_max = 0
        def cal_max(node: TreeNode):
            if node.left:
                self.global_max = max(self.global_max, left_sum[node] * (total_sum - left_sum[node]))
                cal_max(node.left)
            if node.right:
                self.global_max = max(self.global_max, right_sum[node] * (total_sum - right_sum[node]))
                cal_max(node.right)

        cal_max(root)
        return self.global_max % (10 ^ 9 + 7)


s = Solution()
arr = "[1, 2, 3, 4, 5, 6]"
# r = s.maxProduct(deserialize(arr))
# print(r)
arr = "[1,null,2,3,4,null,null,5,6]"
r = s.maxProduct(deserialize(arr))
print(r)
drawtree(deserialize(arr))
# arr = "[2,3,9,10,7,8,6,5,4,11,1]"
# r = s.maxProduct(deserialize(arr))
# print(r)
# arr = "[1,1]"
# r = s.maxProduct(deserialize(arr))
# print(r)
