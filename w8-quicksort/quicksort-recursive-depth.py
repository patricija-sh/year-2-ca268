#
#   qsort code and a partition function.
#
#   Modify the qsort function so that it returns the maximum depth of recursion.
#

def partition(lst, lo, hi):
    part = lo
    while lo < hi:
        while lst[lo] <= lst[part] and lo < hi:
            lo += 1
        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            hi -= 1

        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi]

    # Swap part into position
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        lst[part], lst[hi] = lst[hi], lst[part]
        
    return hi

def rec_qsort(lst, lo, hi):
    if lo >= hi:
        return 0
    else:  # if lo < hi
        pivot = partition(lst, lo, hi)
        left_depth = rec_qsort(lst, lo, pivot - 1) + 1
        right_depth = rec_qsort(lst, pivot + 1, hi) + 1
    
    depth = max(left_depth, right_depth)  # left depth and right depth may not be the same.
    return depth

def qsort(lst):
    return rec_qsort(lst, 0, len(lst) - 1)
