import sys

students = ['ted', 'steve', 'dave', 'dan', 'jack', 'jon', 'will', 'rick', 'adam', 'james', 'bruce']


# Binary search

found = False
min = 0
max = len(students) - 1

search_value = raw_input("What are you searching for?")
print search_value

while found == False:
    avg = (min + max) / 2
    print avg
    if students[avg] == search_value:
        found = True
        print "found"
    elif search_value > students[avg]:
        min = avg + 1
    elif search_value < students[avg]:
        max = avg - 1
