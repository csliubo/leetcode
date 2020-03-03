# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ret = set()
        for num in nums:
            if num in ret:
                ret.remove(num)
            else:
                ret.add(num)
        return ret
