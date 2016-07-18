# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_num = {}
        num_len = nums.__len__()
        if num_len % 2 == 0:
            threshold = num_len / 2
        else:
            threshold = num_len / 2 + 1
        for val in nums:
            count = dict_num.get(val, 0)
            count += 1
            if count >= threshold:
                return val
            dict_num[val] = count
        return None
