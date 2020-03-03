from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        sorted_index = [_[1] for _ in sorted([(num, index) for index, num in enumerate(arr)], key=lambda k: k[0])]
        print(sorted_index)
        arr_len = len(arr)

        def find_left_max(cur, start):
            index = start
            cur_max = None
            for i in range(start - 1, max(0, start - d) - 1, -1):
                if not cur_max:
                    cur_max = arr[i]
                if cur_max < arr[i]:
                    index, cur_max = i, arr[i]
                elif arr[i] >= cur:
                    break
            return index

        def find_left_bound(cur, start):
            i = start
            if i == 0:
                return i
            else:
                i -= 1
            while arr[i] < cur and start < (max(0, start - d) - 1):
                i -= 1
            return i

        def find_right_bound(cur, start):
            i = start
            if i == arr_len - 1:
                return i
            else:
                i += 1
            while arr[i] < cur and i < min(arr_len, start + d):
                i += 1
            return i

        def find_right_max(cur, start):
            index = start
            cur_min = cur
            for i in range(start + 1, min(arr_len, start + d)):
                if cur_min > arr[i]:
                    index, cur_min = i, arr[i]
                elif arr[i] >= cur:
                    break
            return index

        dp = [0 for _ in range(arr_len)]
        for i in sorted_index:
            left_max, right_max = 0, 0
            left = find_left_bound(arr[i], i)
            left_max = max(dp[left:i]) if left and left != i else 0
            right = find_right_bound(arr[i], i)

            right_max = max(dp[i:right]) if right and right != i else 0
            dp[i] = max(left_max, right_max) + 1
            print(arr[i], i, left, right, left_max, right_max)
            print(sorted_index)
            print(arr)
            print(dp)
        return max(dp)


s = Solution()
arr = [6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12]
d = 2
r = s.maxJumps(arr, d)
print(r)
