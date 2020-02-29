# https://leetcode-cn.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        s = 0
        while i < j:
            if height[i] <= height[j]:
                s = max(s, height[i] * (j - i))
                i += 1
            else:
                s = max(s, height[j] * (j - i))
                j -= 1
        return s




if __name__ == '__main__':
    s = Solution()
    a = s.maxArea([2, 3, 4, 5, 18, 17, 6])
    print(a)
