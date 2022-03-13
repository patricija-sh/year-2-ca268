import sys

def make_map():
    input = sys.stdin.readlines()
    grades = {}
    for line in input:
        if line != "\n":
            name, grade = line.rstrip().split()
            grades[name] = grade
    return grades
