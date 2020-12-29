import random

def factorial1(n):
    if n > 1:
        return n*factorial1(n-1)
    return n
def factorial2(n):
    if n == 1:
        return n
    return n*factorial2(n-1)

def add(data):
    if len(data) == 1:
        return data[0]
    return data[0] + add(data[1:]) 


def palindrome(sen):
    if len(sen) <= 1:
        return True
    
    if sen[0] == sen[-1]:
        return palindrome(sen[1:-1])
    else : 
        return False


data = random.sample(range(100), 10)
print(factorial1(5))
print(factorial2(5))
print(data)
print(add(data))
print(palindrome("asdfdf2sa"))