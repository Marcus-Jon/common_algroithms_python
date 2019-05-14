import sys

students = ['ted', 'steve', 'dave', 'dan', 'jack', 'jon', 'will', 'rick', 'adam', 'james', 'bruce']

# Insertion sort

print students
for x in range(0, len(students)):
    value = students[x]
    index = x
    while index > 0 and students[index - 1] > value:
        students[index] = students[index - 1]
        index = index - 1
    students[index] = value
print students
