from Stack import Stack

class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def isempty(self):
        if self.stack1.isempty() and self.stack2.isempty():
            return True
        else:
            return False

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack1.isempty() and self.stack2.isempty():
            return 'Error'
        elif self.stack2.isempty():
            while not self.stack1.isempty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
