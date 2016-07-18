# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        # 转换成map
        return [i for i in set(nums1).intersection(set(nums2))]


nums1 = []
nums2 = []

s = Solution()
print s.intersection(nums1, nums2)

nums1 = [2, 1, 3]
nums2 = []
print s.intersection(nums1, nums2)
nums1 = [2, 1, 3]
nums2 = [2, 2, 3]
print s.intersection(nums1, nums2)
