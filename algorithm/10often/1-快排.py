def qc(nums):
    if len(nums)<1:
        return nums
    l = []
    r = []
    p = nums[0]
    for i in nums:
        if i < p:
            l.append(i)
        elif i > p:
            r.append(i)
    return qc(l) + [p] + qc(r)