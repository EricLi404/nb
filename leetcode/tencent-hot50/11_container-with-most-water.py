# https://leetcode-cn.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        s = 0
        while i < j:
            ns = (j - i) * min(height[i], height[j])
            s = ns if ns > s else s
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return s


class Solution2:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    a = s.maxArea([2, 3, 4, 5, 18, 17, 6])
    print(a)
