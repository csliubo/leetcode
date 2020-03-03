# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        nums.append(-1)
        nums_count = len(nums)
        for num in nums:
            num_int = int(num)
            if 0 <= num_int < nums_count:
                nums[num_int] = str(nums[num_int])

        for index, num in enumerate(nums[1:]):
            if isinstance(num, int):
                return index + 1
        return nums_count
