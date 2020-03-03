# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p1, p2 = nums[0], nums[0]
        while True:
            p1 = nums[p1]
            p2 = nums[nums[p2]]
            if p1 == p2:
                break
        p0 = nums[0]
        while p0 != p1:
            p0, p1 = nums[p0], nums[p1]
        return p1
