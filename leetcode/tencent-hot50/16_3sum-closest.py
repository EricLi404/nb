# https://leetcode-cn.com/problems/3sum-closest
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        mv = sum(nums[:3])
        nums.sort()
        for ii in range(len(nums)):
            i, j = ii + 1, len(nums) - 1
            while i < j:
                # print(nums[i], nums[j], nums[ii])
                av = target - (nums[i] + nums[j] + nums[ii])
                if abs(av) <= abs(target - mv):
                    mv = (nums[i] + nums[j] + nums[ii])
                if av > 0:
                    i += 1
                elif av < 0:
                    j -= 1
                else:
                    return nums[i] + nums[j] + nums[ii]
        return mv


if __name__ == '__main__':
    a = [1, 1, 1, 1]
    # a = [-1, 2, 1, -4]
    t = 0
    s = Solution()
    c = s.threeSumClosest(a, t)
    print(c)
