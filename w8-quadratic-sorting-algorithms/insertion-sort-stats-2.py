def insertion_sort(lst):
    
    move_count = 0
    comparison_count = 0
    for todo in range(1, len(lst)):
        tobeinserted = lst[todo]
        i = todo
        while i > 0 and tobeinserted < lst[i-1]:
            lst[i] = lst[i-1] # Make space for the item
            comparison_count += 1
            move_count += 1
            i -= 1
        lst[i] = tobeinserted  # Found the place for this item, plonk it in.
        
        if i > 0:
            comparison_count += 1
        move_count += 2
        
    return comparison_count, move_count
