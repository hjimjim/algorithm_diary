import random

def bubble_sort(data):
    for j in range(len(data)-1):
        swap = False
        for i in range(len(data)-j-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]      
                swap = True
        if not swap:
            break
        
    return data

data = random.sample(range(100), 5)
print(data)
print(bubblesort(data))
