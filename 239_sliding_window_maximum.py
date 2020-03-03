# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 1:
            return nums
        window, ret = [], []
        for i, num in enumerate(nums):
            # 去除windows最左边已经要干掉的元素
            if i >= k and window[0] <= i - k:
                window.pop(0)
            while window and nums[window[-1]] < num:
                window.pop()
            window.append(i)
            if i >= k - 1:
                ret.append(nums[window[0]])
        return ret


if __name__ == "__main__":
    s = Solution()

    l1 = [1, 2, 3]
    print(s.maxSlidingWindow(l1, 2))
    l1 = [1, 3, -1, -3, 5, 3, 6, 7]
    print(s.maxSlidingWindow(l1, 3))
