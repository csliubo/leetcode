# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def is_even_len(self, arr):
        return arr.__len__() % 2 == 0

    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1 and not nums2:
            return None
        if not nums1 or nums1.__len__() == 0:
            ret = self.get_median(nums2)
        elif not nums2 or nums2.__len__() == 0:
            ret = self.get_median(nums1)
        else:
            ret = self._findMedianSortedArrays(nums1, nums2)
        return ret

    def get_median(self, arr):
        if arr.__len__() == 1:
            return arr[0]
        if arr.__len__() % 2 != 0:
            return arr[arr.__len__() / 2]
        else:
            return (arr[arr.__len__() / 2] + arr[(arr.__len__() / 2) - 1]) / 2.0

    def _findMedianSortedArrays(self, nums1, nums2):
        """
        :type arr_one: List[int]
        :type arr_two: List[int] arr_two.__len__() <= arr_one.__len__()
        :rtype: float
        """

        if nums1.__len__() < nums2.__len__():
            arr_long = nums2
            arr_short = nums1
        else:
            arr_long = nums1
            arr_short = nums2

        arr_long_len = arr_long.__len__()
        arr_short_len = arr_short.__len__()

        # 如果两个数组没有交集,则直接取中间的值
        if arr_long[arr_long_len - 1] <= arr_short[0] or arr_short[arr_short_len - 1] <= arr_long[0]:
            if arr_long[arr_long_len - 1] <= arr_short[0]:
                small_arr = arr_long
                larger_arr = arr_short
            else:
                small_arr = arr_short
                larger_arr = arr_long
            if (arr_long_len + arr_short_len) % 2 == 0:
                # 取左右边界的值,再除于2
                left_index = (arr_long_len + arr_short_len) / 2 - 1
                right_index = (arr_long_len + arr_short_len) / 2
                if left_index > small_arr.__len__() - 1:
                    left = larger_arr[left_index - small_arr.__len__()]
                else:
                    left = small_arr[left_index]
                if right_index > small_arr.__len__() - 1:
                    right = larger_arr[right_index - small_arr.__len__()]
                else:
                    right = small_arr[right_index]
                return (left + right) / 2.0
            else:
                middle = (small_arr.__len__() + larger_arr.__len__() - 1) / 2
                if middle > small_arr.__len__() - 1:
                    return larger_arr[middle - small_arr.__len__()]
                return small_arr[middle]

        if self.is_even_len(arr_long):
            left_bound_long = arr_long[arr_long_len / 2 - 1]
            right_bound_long = arr_long[arr_long_len / 2]
            arr_long_median = (left_bound_long + right_bound_long) / 2.0
        else:
            left_bound_long = arr_long[arr_long_len / 2 - 1]
            right_bound_long = arr_long[arr_long_len / 2 + 1]
            arr_long_median = arr_long[arr_long_len / 2]

        # 其中一个数组只有一个元素
        if arr_short.__len__() == 1:
            arr_short_median = arr_short[0]
            result_arr = [right_bound_long, left_bound_long, arr_short[0]]

            if not self.is_even_len(arr_long):
                result_arr.append(arr_long_median)

            result_arr = sorted(result_arr)
            result_arr_len = result_arr.__len__()
            if result_arr_len % 2 != 0:
                return result_arr[result_arr_len / 2]
            else:
                return (result_arr[result_arr_len / 2 - 1] + \
                        result_arr[result_arr_len / 2]) / 2.0

        # 取需要比较的边界值和中值
        if self.is_even_len(arr_short):
            left_bound_short = arr_short[arr_short_len / 2 - 1]
            right_bound_short = arr_short[arr_short_len / 2]
            arr_short_median = (left_bound_short + right_bound_short) / 2.0
        else:
            left_bound_short = arr_short[arr_short_len / 2 - 1]
            right_bound_short = arr_short[arr_short_len / 2 + 1]
            arr_short_median = arr_short[arr_short_len / 2]

        # 判断是否为中位数
        if left_bound_long <= arr_short_median <= right_bound_long or left_bound_short <= arr_long_median <= right_bound_short:

            result_arr = [left_bound_short, left_bound_long, right_bound_short, right_bound_long]

            if not self.is_even_len(arr_long):
                result_arr.append(arr_long_median)

            if not self.is_even_len(arr_short):
                result_arr.append(arr_short_median)

            result_arr = sorted(result_arr)
            result_arr_len = result_arr.__len__()
            if result_arr_len % 2 != 0:
                return result_arr[result_arr_len / 2]
            else:
                return (result_arr[result_arr_len / 2 - 1] + \
                        result_arr[result_arr_len / 2]) / 2.0
        else:
            # 不是中位数,继续找
            # 判断方向
            if arr_short_median < left_bound_long:
                # short向右 long向左
                new_nums2 = arr_short[arr_short_len / 2:]
                offset = arr_short_len - new_nums2.__len__()
                new_nums1 = arr_long[:arr_long_len - offset]
                return self._findMedianSortedArrays(new_nums1, new_nums2)
            elif arr_short_median > right_bound_long:
                new_nums2 = arr_short[:arr_short_len / 2]
                offset = arr_short_len - new_nums2.__len__()
                new_nums1 = arr_long[offset:]
                return self._findMedianSortedArrays(new_nums1, new_nums2)


s = Solution()
# nums1 = [1, 3, 5, 7]
# nums2 = [8, 9, 10, 11, 12, 13]
# s.findMedianSortedArrays(nums1, nums2)
# nums1 = [8, 10, 11, 12, 13]
# nums2 = [1, 3, 5, 7]
# s.findMedianSortedArrays(nums1, nums2)

nums1 = [1, 2, 3, 4, 9]
nums2 = [6, 7]

s.findMedianSortedArrays(nums1, nums2)

nums1 = [1, 2, 3, 4, 9]
nums2 = []

s.findMedianSortedArrays(nums1, nums2)
nums1 = [1]
nums2 = []

nums1 = [2]
nums2 = [1, 3, 4, 5]

s.findMedianSortedArrays(nums1, nums2)

nums1 = [1, 3]
nums2 = [2, 4, 5, 6]

s.findMedianSortedArrays(nums1, nums2)

nums1 = [3, 5, 6]
nums2 = [1, 2, 4]
s.findMedianSortedArrays(nums1, nums2)

nums1 = [1, 2, 4]
nums2 = [3, 5, 6, 7]
s.findMedianSortedArrays(nums1, nums2)
