# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cur_sum = 0
        cur_max = 0
        for num in nums:
            cur_sum+=num
            cur_max = max(num, cur_max)
        if cur_max == len(nums)-1:
            return len(nums)
        return int((cur_max*(cur_max+1))/2) - cur_sum