# https://leetcode-cn.com/problems/3sum/

# 给定一个数组和目标数target，找出数组中a,b,c满足 a+b+c = target 的所有组合。例如：arr = [-3,-1,-2,1,2,3]，target = 0。输出为 [(-3,1,2),(-2,-1,3)]

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ln = len(nums)
        nums.sort()
        s = set()
        for i1 in range(ln):
            i, j = i1 + 1, ln - 1
            while i < j:
                if nums[i1] + nums[i] + nums[j] < 0:
                    i += 1
                elif nums[i1] + nums[i] + nums[j] > 0:
                    j -= 1
                else:
                    s.update({(nums[i1], nums[i], nums[j])})
                    i += 1
                    j -= 1
        return [list(a) for a in s]


if __name__ == '__main__':
    s = Solution()
    c = s.threeSum([-1, 0, 1, 2, -1, -4])
    print(c)
