class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)

def check_brackets(line):
    stack = Stack()
    assert stack.is_empty()
    for c in line:
        try:
            if c == '(':
                stack.push(c)
            elif (stack.top() == '(' and c == ')'):
                stack.pop()
        except IndexError:
            if c == ')':
                return False
    return stack.is_empty()
