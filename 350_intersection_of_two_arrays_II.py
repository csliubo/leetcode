# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []

        dict_nums1 = {}
        for val in nums1:
            count = dict_nums1.get(val, 0)
            count += 1
            dict_nums1[val] = count

        ret = []
        for val in nums2:
            count = dict_nums1.get(val, 0)
            if count > 0:
                ret.append(val)
                dict_nums1[val] = count - 1

        return ret