class Solution:
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n = nums1 + nums2
        n.sort()
        l = len(n)
        return n[l // 2] if l % 2 == 1 else (n[l // 2] + n[l // 2 - 1]) / 2


if __name__ == '__main__':
    ss = Solution()
    n1 = [1, 3]
    n2 = [2, 4]
    cc = ss.findMedianSortedArrays(n1, n2)
    print(cc)
