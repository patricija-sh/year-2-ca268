def print_queue(q, front, back):
    if front < back:
        return q[front:back]
    elif front > back:
        return q[front:] + q[:back]
