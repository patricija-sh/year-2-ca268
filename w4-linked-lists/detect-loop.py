def detect_loop(lst):
    if lst.is_empty():
        return False
    else:
        tmp = lst.head
        while tmp.next is not None and tmp.next != lst.head:
            tmp = tmp.next
        return tmp.next == lst.head
