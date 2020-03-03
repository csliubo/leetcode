# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        ret = []
        nums.sort()
        for i, x in enumerate(nums[:-2]):
            tmp_sum = {}
            added_val = set()
            if i >= 1 and x == nums[i - 1]:
                continue
            for k, v in enumerate(nums[i + 1:]):
                if v in tmp_sum and v not in added_val:
                    ret.append((x, v, -x - v))
                    added_val.add(v)
                else:
                    tmp_sum[-x - v] = 1
        return ret


if __name__ == "__main__":
    s = Solution()

    # l1 = [1, 2, 3]
    # print(s.threeSum(l1))
    # l1 = [-1, 0, 1, 2, -1, -4]
    # print(s.threeSum(l1))
    l1 = [0, 0, 0, 0]
    print(s.threeSum(l1))
