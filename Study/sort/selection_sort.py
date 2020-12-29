import random, sys

def selection_sort(data):
    for i in range(len(data)-1):
        index = i
        for j in range(i+1, len(data)):
            if data[index] > data[j]:
                index = j
        data[i], data[index] = data[index], data[i]
    return data



data = random.sample(range(100), 5)
print(data)
print(selection_sort(data)))