# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):

    _cache_ = {

    }
    def _do_rob_(self, nums):
        if not nums:
            return 0
        nums_len = nums.__len__()
        if nums_len == 1:
            return nums[0]
        if nums_len == 2:
            return max(nums[0], nums[1])
        if nums_len in self._cache_:
            return self._cache_[nums_len]
        ret = max(nums[0] + self._do_rob_(nums[2:]), self._do_rob_(nums[1:]))
        self._cache_[nums_len] = ret
        return ret

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self._cache_ ={}
        return self._do_rob_(nums)



nums = [1, 3, 4, 2, 8]
s = Solution()
print s.rob(nums)
nums = [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81,
        185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]
s = Solution()
print s.rob(nums)
nums = [1, 1, 1]
s = Solution()
print s.rob(nums)
