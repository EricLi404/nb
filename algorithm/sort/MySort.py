def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
    return nums


def selection_sort(nums):
    for i in range(len(nums) - 1):
        mik = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[mik]:
                mik = j
        nums[i], nums[mik] = nums[mik], nums[i]

    return nums


if __name__ == '__main__':
    ll = [3, 2, 4, 7, 1]
    # print(bubble_sort(ll))
    print(selection_sort(ll))
