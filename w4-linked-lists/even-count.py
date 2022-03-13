def even_count(lst):
    curNode = lst.head
    total = 0
    while curNode is not None:
        total += (curNode.item + 1) % 2
        curNode = curNode.next
    return total
