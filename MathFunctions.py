def min(lst):
    min = lst[1]
    for num in lst:
        if min > num:
            min = num
    return min

def max(lst):
    max = lst[1]
    for num in lst:
        if max < num:
            max = num
    return max

def average(lst):
    total = 0
    for num in lst:
        total += num
    return total / len(lst)

def sort(lst):
    sorted = False
    high = len(lst) - 1
    while not sorted and high > 1:
        sorted = True
        for i in range(high):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                sorted = False
        high -= 1
    return lst

def median(lst):
    lst = sort(lst)
    if len(lst) % 2 == 1:
        return lst[floor(len(lst) / 2)]
    else:
        return (lst[len(lst) / 2 - 1] + lst[len(lst) / 2]) / 2

def mode(lst):
    dictionary = {}
    for num in lst:
        if num in dictionary:
            dictionary[num] += 1
        else:
            dictionary[num] = 1
    num = 0
    amount = 0
    for key, value in dictionary.items():
        if value > amount:
            num = key
            amount = value
    return num

def abs(num):
    if num > 0:
        return num
    elif num < 0:
        return num * -1
    else:
        return 0

def exponent(num, power):
    match power:
        case 0:
            return 1
        case 1:
            return num
        case _:
            total = num
            for i in range(power - 1):
                total *= num
            return total

def round(num):
    if num % 1 >= .5:
        return num - num%1 + 1
    else:
        return num - num%1

def floor(num):
    return num - num%1

def ceil(num):
    return num + (1 - num%1)

def sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

def pi():
    return 3.14159265358979323846264

def factorial(num):
    for i in range(num - 1, 1, -1):
        num *= i
    return num

def power(num, exp):
    times = num
    for i in range(exp):
        num *= times
    return num

