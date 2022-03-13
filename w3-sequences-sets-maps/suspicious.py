import sys

with open(sys.argv[1], 'r') as f:
    students = set([w.rstrip() for w in f.readlines()])

with open(sys.argv[2], 'r') as f:
    delinquents = set([w.rstrip() for w in f.readlines()])

sus = sorted(students.intersection(delinquents))

for i in range(len(sus)):
    print(f"{i+1}. {sus[i]}")
