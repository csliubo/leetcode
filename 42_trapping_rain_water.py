# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        max_index, last_max = 0, 0
        for i, h in enumerate(height):
            if h > last_max:
                last_max, max_index = h, i
        if last_max == 0:
            return 0
        left_part = height[:max_index + 1]
        right_part = [h for h in reversed(height[max_index:])]

        return self.trap1(left_part) + self.trap1(right_part)

    def trap1(self, height: List[int]) -> int:
        if not height:
            return 0

        start, end = 0, 0
        for i, h in enumerate(height):
            if h != 0:
                start = i
                break
        else:
            return 0
        len_height = len(height)
        if start == len_height - 1:
            return 0
        end = start + 1
        drop_count = 0
        start_height = height[start]
        height_in_middle = 0
        while end < len_height:
            end_height = height[end]
            if end_height >= start_height:
                drop_count += (end - start - 1) * start_height - height_in_middle
                start, start_height, height_in_middle = end, end_height, 0
            else:
                height_in_middle += end_height
            end += 1
        return drop_count


s = Solution()
l = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
result = s.trap(l)
print(result)
assert result == 6
