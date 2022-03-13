from Node import Node

def add_to_queue(head, item):
    new_node = Node(item, None)

    if head is None:
        head = new_node
    else:
        curNode = head
        while curNode.next is not None:
            curNode = curNode.next
        curNode.next = new_node
