import sys

students = ['ted', 'steve', 'dave', 'dan', 'jack', 'jon', 'will', 'rick', 'adam', 'james', 'bruce']

temp = ''
for i in range(len(students) - 1):
    for j in range(len(students) - i - 1):
        if students[j] > students[j + 1]:
            temp = students[j]
            students[j] = students[j + 1]
            students[j + 1] = temp
print students
