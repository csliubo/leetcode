# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        nums_len = len(nums)
        left, right = 0, nums_len - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid
        # exit(0)
        print(left, right)
        if left == right:
            return self.binary_search(nums, target)
        if nums[0] <= target <= nums[max(0, left - 1)]:
            return self.binary_search(nums[:max(1, left)], target)
        else:
            right_pos = self.binary_search(nums[max(1, left):], target)
            if right_pos > -1:
                return right_pos + left
            else:
                return -1

    def binary_search(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        left, right = 0, nums_len - 1
        while left <= right:
            if left == right:
                return left if nums[left] == target else -1
            mid = left + (right - left + 1) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


s = Solution()
l = [1]
k = 1
l = [3, 1]
k = 3
print(s.search(l, k))
