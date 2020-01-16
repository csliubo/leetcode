# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        sum = 0
        for i in range(0, nums.__len__(), 2):
            sum += nums[i]

        return sum


nums = [3, 2, 1, 4]

s = Solution()
print s.arrayPairSum(nums)
