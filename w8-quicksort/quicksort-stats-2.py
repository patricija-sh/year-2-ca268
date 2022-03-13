#
#   qsort code and a partition function.
#
#   Modify the code so that it returns the number of compares and the number of moves.
#
comparison_count = 0
swap_count = 0

def partition(lst, lo, hi):
    global comparison_count
    global swap_count
    
    lst[lo], lst[(hi+lo)//2] = lst[(hi+lo)//2], lst[lo]
    swap_count += 3
    part = lo
    while lo < hi:
        comparison_count += 2
        while lst[lo] <= lst[part] and lo < hi:
            comparison_count += 1
            lo += 1
        
        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            comparison_count += 1
            hi -= 1

        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi]
            swap_count += 3

    # Swap part into position
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        lst[part], lst[hi] = lst[hi], lst[part]
        swap_count += 3

    comparison_count += 1
    return hi

def rec_qsort(lst, lo, hi):
    if lo < hi:
        pivot = partition(lst, lo, hi)
        rec_qsort(lst, lo, pivot - 1)
        rec_qsort(lst, pivot + 1, hi)

def qsort(lst):
    rec_qsort(lst, 0, len(lst) - 1)
    return comparison_count, swap_count
