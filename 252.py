from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals or len(intervals) == 1:
            return True
        sorted_intervals = sorted(intervals, key=lambda k: k[0])
        last_end = sorted_intervals[0][1]
        for interval in sorted_intervals[1:]:
            if last_end > interval[0]:
                return False
            last_end = interval[1]
        return True
