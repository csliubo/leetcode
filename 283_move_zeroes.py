# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_index = -1
        for i in range(0, nums.__len__()):
            if nums[i] == 0 and zero_index < 0:
                zero_index = i
            if nums[i] != 0 and zero_index >= 0 and i != zero_index:
                tmp = nums[i]
                nums[zero_index] = tmp
                nums[i] = 0
                zero_index += 1


nums = [0, 1, 0, 3, 12]

s = Solution()
s.moveZeroes(nums)
print nums

nums = [0, 1, 0, 3, 12, -1, 0, 0, 0, 0, 8, 99, 2, 0, 0]
s.moveZeroes(nums)
print nums

nums = [1, 2, 3]
s.moveZeroes(nums)
print nums
