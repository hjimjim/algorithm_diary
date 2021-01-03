import random

def binary_search(data, search):
    if len(data) == 1 and search == data[0]:
        return True
    elif len(data) == 1 and search != data[0]:
        return False
    elif len(data) == 0:
        return False

    index = len(data)//2
    find = data[index]
    if search == find:
        return True
    else: 
        if search < find:
            return binary_search(data[:index], search)
        elif search > find:
            return binary_search(data[index+1:],search)
    
data = random.sample(range(100), 5)
data.sort()
search = random.sample(range(100), 1)
print(data, search[0])
print(binary_search(data, search[0]))
