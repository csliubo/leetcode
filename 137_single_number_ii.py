# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = {}
        for num in nums:
            if num in s:
                if s[num] == 2:
                    del s[num]
                else:
                    s[num] += 1
            else:
                s[num] = 1
        for n in s:
            return n
