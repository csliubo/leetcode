# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            if target - num in nums_dict:
                return [nums_dict[target - num], i]
            nums_dict[num] = i

    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}

    def twoSum2(self, nums, target):
        pos = {}
        pos_2 = {}
        for i in range(0, nums.__len__()):
            val = nums[i]
            if val in pos:
                pos_2[val] = i
            else:
                pos[val] = i

        # print pos
        sorted_nums = sorted(nums)

        # print sorted_nums
        left = 0
        right = sorted_nums.__len__() - 1
        while left != right:
            left_val = sorted_nums[left]
            right_val = sorted_nums[right]
            res = left_val + right_val
            if res == target:
                left_index = pos.get(sorted_nums[left]) + 1

                if left_val == right_val:
                    right_index = pos_2.get(sorted_nums[right]) + 1
                else:
                    right_index = pos.get(sorted_nums[right]) + 1

                if left_index > right_index:
                    return [right_index, left_index]
                return [left_index, right_index]

            if res > target:
                right -= 1
            else:
                left += 1


s = Solution()
numbers = [3,0,3,1,2]
target = 6
print(s.twoSum(numbers, target))
