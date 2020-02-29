def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
    return nums


def quick_sort(nums):
    if len(nums) < 1:
        return nums
    p = nums[0]
    l = []
    r = []
    for i in nums:
        if i < p:
            l.append(i)
        elif i > p:
            r.append(i)
    return quick_sort(l) + [p] + quick_sort(r)


def selection_sort(nums):
    for i in range(len(nums) - 1):
        mik = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[mik]:
                mik = j
        nums[i], nums[mik] = nums[mik], nums[i]

    return nums


def BubbleSort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                (lst[j], lst[j + 1]) = (lst[j + 1], lst[j])


if __name__ == '__main__':
    ll = [4, 8, 1, 3, 2, 9, 7]
    # print(bubble_sort(ll))
    print(quick_sort(ll))
