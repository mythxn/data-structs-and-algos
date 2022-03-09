# 0(n)
def linear_search(nums, target):
    for i, e in enumerate(nums):
        if e == target:
            return i
    return -1


# Θ(log(n))
def binary_search(nums, target):
    left_p = 0
    right_p = len(nums) - 1

    while left_p <= right_p:
        mid = (left_p + right_p) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left_p = mid + 1
        else:
            right_p = mid - 1
    return -1