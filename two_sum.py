# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
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
numbers = [-1,-2,-3,-4,-5]
target = -8
print s.twoSum(numbers, target)