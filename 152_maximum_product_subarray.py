# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]
        for num in nums[1:]:
            cur_max, cur_min = max(cur_max*num, cur_min*num, num), min(cur_max*num, cur_min*num, num)
            global_max = max(cur_max, global_max)
        return global_max