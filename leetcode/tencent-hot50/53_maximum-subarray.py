# https://leetcode-cn.com/problems/maximum-subarray
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxv = nums[0]
        c_maxv = nums[0]
        for i in nums[1:]:
            if c_maxv > 0:
                c_maxv += i
            else:
                c_maxv = i
            maxv = max(maxv, c_maxv)
        return maxv





if __name__ == '__main__':
    s = Solution()
    a = s.maxSubArray([1])
    # a = s.maxSubArray([-2,1])
    print(a)
