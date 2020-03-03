from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        temp_ret = [0] * len(nums)
        count = 0

        