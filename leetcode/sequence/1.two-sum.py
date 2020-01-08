class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            try:
                cc = nums.index(target - nums[i])
            except Exception:
                continue
            else:
                if i != cc:
                    return [i, cc]


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    ss = Solution()
    ccc = ss.twoSum(nums, target)
    print(ccc)
