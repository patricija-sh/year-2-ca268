from Stack import Stack
import sys

def reverse_input(stack):
    # Your code here
    # Read the input
    input = sys.stdin.readlines()
    for line in input:
        stack.push(line)
    while not stack.is_empty():
        print(stack.pop(), end='')
    # place on the stack
    # print from the stack
