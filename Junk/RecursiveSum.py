nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def sumList(n):
    if n > 0:
        return nums[n] + sumList(n-1)
    else:
        return 0


s = sumList(len(nums)-1)
print(s)