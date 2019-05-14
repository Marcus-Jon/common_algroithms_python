def quick_sort(list):
    helper(list, 0, len(list) - 1)

def helper(list, first, last):
    if first < last:
        split = partion(list, first, last)

        helper(list, first, split - 1)
        helper(list, split + 1 , last)

def partion(list, first, last):
    pivot = list[first]
    leftmark = first + 1
    rightmark = last

    done = False

    while done == False:
        while leftmark <= rightmark and list[leftmark] <= pivot:
            leftmark = leftmark + 1
        while rightmark >= leftmark and list[rightmark] >= pivot:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            temp = list[leftmark]
            list[leftmark] = list[rightmark]
            list[rightmark] = temp

    temp = list[first]
    list[first] = list[rightmark]
    list[rightmark] = temp

    return rightmark

list = [54, 26, 93, 17, 77, 31, 44, 55, 67]
print list
quick_sort(list)
print list
