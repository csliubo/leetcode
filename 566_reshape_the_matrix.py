# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums:
            return nums
        origin_row_count = nums.__len__()
        origin_col_count = nums[0].__len__()
        if r * c != origin_row_count * origin_col_count:
            return nums
        ret = []
        for i in range(0, r):
            cols = []
            for j in range(0, c):
                current_pos = i * c + j
                origin_row = current_pos / origin_col_count
                origin_col = current_pos % origin_col_count
                cols.append(nums[origin_row][origin_col])

            ret.append(cols)
        return ret


s = Solution()
print s.matrixReshape([[1, 2], [3, 4]], 4, 1)
