class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target: int):
        dd = {}
        for i in range(len(nums)):
            dd[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in dd and dd[target - nums[i]] != i:
                return [i, dd[target - nums[i]]]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    ss = Solution()
    ccc = ss.twoSum(nums, target)
    print(ccc)
