# Written 23-June-2020
# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python

def dig_pow(n, p):
    total = sum([int(str(n)[i])**(p+i) for i in range(len(str(n)))]) 
    return total / n if (total % n) == 0 else -1
