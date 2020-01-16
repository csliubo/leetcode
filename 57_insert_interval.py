# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "(%s, %s)" % (self.start, self.end)


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]

        current_interval = intervals[0]
        last_interval = intervals[-1]
        if newInterval.start <= current_interval.start and newInterval.end >= last_interval.end:
            return [newInterval]

        if newInterval.start < current_interval.start:
            if newInterval.end < current_interval.start:
                # 区间不覆盖, new interval在前面,直接插入到结果中
                intervals.insert(0, newInterval)
                return intervals
            elif current_interval.start <= newInterval.end <= current_interval.end:
                intervals.pop(0)

                intervals.insert(0, Interval(newInterval.start, current_interval.end))
                return intervals
            else:
                return self.insert(intervals[1:], newInterval)
        elif current_interval.start <= newInterval.start <= current_interval.end:
            if newInterval.end <= current_interval.end:
                return intervals
            else:
                return self.insert(intervals[1:], Interval(current_interval.start, newInterval.end))
        else:
            ret = []
            ret.append(current_interval)
            ret.extend(self.insert(intervals[1:], newInterval))
            return ret


s = Solution()
lst = list()
# [1,2],[3,5],[6,7],[8,10],[12,16]
lst.append(Interval(1, 2))
lst.append(Interval(3, 5))
lst.append(Interval(6, 7))
lst.append(Interval(8, 10))
lst.append(Interval(12, 16))
print s.insert(lst, Interval(3, 9))
