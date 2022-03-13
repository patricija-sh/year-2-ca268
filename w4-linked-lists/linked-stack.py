from LinkedList import LinkedList

class LinkedStack:
    def __init__(self):
        self.ll = LinkedList()
        
    def push(self, item):
        self.ll.add(item)
        
    def pop(self):
        if self.is_empty():
            return None
        else:
            out = self.ll.head.item
            self.ll.remove()
            return out
        
    def is_empty(self):
        return self.ll.head == None
