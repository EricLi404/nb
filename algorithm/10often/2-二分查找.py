def bs(nums,t):
    s,e = 0,len(nums)-1
    while True:
        if e-s <=1:
            return e if e == t else s
        mid = (s+e)//2
        if mid <= t:
            s = mid
        else:
            e = mid


if __name__ == '__main__':
    cc = bs([1, 3, 4, 5, 6, 8, 9], 8)
    print(cc)