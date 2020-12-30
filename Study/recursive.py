import random

def factorial1(n):
    if n > 1:
        return n*factorial1(n-1)
    return n
def factorial2(n):
    if n == 1:
        return n
    return n*factorial2(n-1)

def palindrome(sen):
    if len(sen) <= 1:
        return True
    
    if sen[0] == sen[-1]:
        return palindrome(sen[1:-1])
    else : 
        return False

def practice(data):
    if len(data) == 1:
        return data[0]
    return data[0] + add(data[1:]) 

def practice1(num):
    print(num)
    if num == 1:
        return 1

    if num%2 == 0:
        return practice(int(num/2))
    else:
        return practice(3*num + 1)

def practice2(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    return practice2(num-1) + practice2(num-2) + practice2(num-3)


data = random.sample(range(100), 10)
print(factorial1(5))
print(factorial2(5))
print(data)
print(add(data))
print(palindrome("asdfdf2sa"))
practice1(3)
print(practice2(4))