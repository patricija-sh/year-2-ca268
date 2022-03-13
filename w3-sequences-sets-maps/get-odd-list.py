import sys

def get_odd_list():
    i = 0
    nums = sys.stdin.readlines()
    odd_nums = []
    while int(nums[i]) != -1:
        if int(nums[i]) % 2 == 1:
            odd_nums.append(int(nums[i]))
        i += 1
    return odd_nums
