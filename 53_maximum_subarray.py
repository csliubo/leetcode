# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    # 使用dp
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_to_now = max_global = nums[0]
        for num in nums[1:]:
            max_to_now = max(max_to_now + num, num)
            max_global = max(max_to_now, max_global)
        return max_global


s = Solution()
l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = s.maxSubArray(l)
print(result)
assert result == 6
