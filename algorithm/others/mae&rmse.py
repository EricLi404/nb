import math
from typing import List


def RMSE(records):
    return math.sqrt(sum([(rui - pui) ** 2 for _, _, rui, pui in records]) / (len(records)))


def MAE(records):
    return sum([abs(rui - pui) for _, _, rui, pui in records]) / len(records)


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        mv = nums[0]
        nums = nums[1:]
        nv = sum(nums)
        ml = [mv]
        for i in range(len(nums)):
            if mv > nv:
                return ml
            ml.append(nums[i])
            mv += nums[i]
            nv -= nums[i]
        return ml


if __name__ == '__main__':
    s = Solution()
    a = s.minSubsequence([4,3,10,9,8])
    print(a)
