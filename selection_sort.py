import sys

students = ['ted', 'steve', 'dave', 'dan', 'jack', 'jon', 'will', 'rick', 'adam', 'james', 'bruce']

# Selection sort
print students
for x in range(len(students)):
    # set minimum value and the index of it
    min_index = x
    min_value = students[x]

    for y in range(x + 1, len(students)):
        # compare minimum value with the next value, to find the smallest value
        # change minimum when found
        if min_value > students[y]:
            min_index = y
            min_value = students[y]
    # move the smallest unsorted value to the start of the list
    students[x], students[min_index] = students[min_index], students[x]

print students
