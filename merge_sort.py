import sys

students = ['ted', 'steve', 'dave', 'dan', 'jack', 'jon', 'will', 'rick', 'adam', 'james', 'bruce']

# Merge sort

def mergesort(students):
    if len(students) > 1:
        midpoint = len(students) // 2
        left = students[:midpoint]
        right = students[midpoint:]

        mergesort(left)
        mergesort(right)

        x = 0
        y = 0
        z = 0

        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                students[z] = left[x]
                x = x + 1
            else:
                students[z] = right[y]
                y = y + 1
            z = z + 1
        while x < len(left):
            students[z] = left[x]
            x = x + 1
            z = z + 1
        while y < len(right):
            students[z] = right[y]
            y = y + 1
            z = z + 1

mergesort(students)
print students
