import random
def split(data):
    if len(data) <= 1:
        return data
    
    medium = int(len(data)/2)
    left = data[:medium] 
    right = data[medium:]

    return merge(split(left), split(right))

def merge(left, right):
    result = list()
    left_point, right_point = 0, 0
    while len(left) > left_point and len(right) > right_point: 
        if left[left_point] < right[right_point]:
            result.append(left[left_point])
            left_point += 1
        else:
            result.append(right[right_point])
            right_point += 1

    while len(left) > left_point:
         result.append(left[left_point])
         left_point += 1

    while len(right) > right_point:
        result.append(right[right_point])
        right_point += 1

    return result


data = random.sample(range(100), 5)
print(data)
print(split(data))
