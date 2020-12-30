import random

def quick_sort1(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left,right = list(), list()
    for i in range(1, len(data)):
        if pivot >= data[i]:
            left.append(data[i])
        else:
            right.append(data[i])

    return quick_sort1(left) + [pivot] + quick_sort1(right)

def quick_sort2(data):
    if len(data) <= 1:
        return data
    pivot = data[0]

    left = [number for number in data[1:] if number < pivot]
    right = [number for number in data[1:] if number >= pivot]

    return quick_sort2(left) + [pivot] + quick_sort2(right)

data = random.sample(range(100), 5)
print(quick_sort1(data))
print(quick_sort2(data))
