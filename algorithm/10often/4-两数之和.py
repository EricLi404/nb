from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            j = d.get(target - nums[i], -1)
            if j != -1:
                return [j, i]
            else:
                d[nums[i]] = i
        return []
