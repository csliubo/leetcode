# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        last = nums[0]
        nums_size = len(nums)
        for i in range(1, nums_size):
            if nums[i] == last:
                break
            last = nums[i]
        else:
            return nums_size
        last_index = i - 1
        swap_start_index = i
        for i in range(swap_start_index, nums_size):
            if nums[i] == last:
                continue
            last_index += 1
            nums[last_index] = nums[i]
            last = nums[i]
        return last_index + 1
    # def move(self, nums, ):


if __name__ == "__main__":
    s = Solution()
    l = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(s.removeDuplicates(l))
    l = [1, 1, 2, 3]
    print(s.removeDuplicates(l))
