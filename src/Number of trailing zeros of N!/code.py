# Written: 22-Apr-2020
# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/python

def zeros(n):
    count = 0
    pow = 5
    while (n / pow >= 1):
        count += int(n / pow)
        pow *= 5

    return int(count)
