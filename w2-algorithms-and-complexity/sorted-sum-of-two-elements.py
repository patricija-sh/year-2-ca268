def sum_to_k(list, k):
    start = 0
    end = len(list) - 1
    looper = 0
    if len(list) == 1:
        return False
    while looper < len(list):
        if start == end:
            return False
        elif list[start] + list[end] > k:
            end = end - 1
        elif list[start] + list[end] < k:
            start += 1
        else:
            return True
        looper += 1
    if looper == len(list):
        return False
