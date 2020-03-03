# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = nums[0]
        for num in nums[1:]:
            ret ^= num
        return ret