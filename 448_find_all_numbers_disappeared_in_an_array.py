# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        if nums.__len__() == 1:
            return nums

        nums_len = nums.__len__()
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        return [i + 1 for i in range(0, nums_len) if nums[i] > 0]


s = Solution()

lst = [4, 3, 2, 7, 8, 2, 3, 1]
print s.findDisappearedNumbers(lst)
