def fibonacci_recursive(data):
    if data <= 1:
        return data
    
    return fibonacci_recursive(data - 1) + fibonacci_recursive(data - 2)

def fibonacci_dp(data):
    cache = [0 for index in range(data+1)]
    cache[1] = 1
    for i in range(2, data+1):
        cache[i] = cache[i-1] + cache[i-2]
    
    return cache[data]

print(fibonacci_recursive(10))
print(fibonacci_dp(10))