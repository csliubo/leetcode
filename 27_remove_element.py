# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 设置头尾指针,
        if not nums:
            return 0
        nums_len = nums.__len__()
        if nums_len == 1:
            if nums[0] == val:
                nums = []
                return 0
            else:
                return 1
        head = 0
        tail = nums_len - 1

        while head < tail:
            for i in range(head, nums_len):
                if nums[i] == val:
                    break
            head = i
            for i in range(tail, -1, -1):
                if nums[i] != val:
                    break
            tail = i
            if (head == tail == 0):
                nums = []
                return 0
            if (head == tail == (nums_len - 1)):
                if nums[head] == val:
                    nums = nums[:head - 1]

                return nums.__len__()
            if head < tail:
                tmp = nums[tail]
                nums[tail] = nums[head]
                nums[head] = tmp
                head += 1
                tail -= 1
            if head > tail:
                nums = nums[:head]
                break
            if head == tail:
                if nums[head] == val:
                    nums = nums[:head]
                else:
                    nums = nums[:head + 1]

        return nums.__len__()


nums = [3, 2, 2, 3, 0]
val = 3
s = Solution()
# print s.removeElement(nums, val), nums
#
# nums = [1, 1, 1, 3, 2, 2, 3]
# val = 4
# print s.removeElement(nums, val), nums
nums = [4]
val = 4
print s.removeElement(nums, val), nums
