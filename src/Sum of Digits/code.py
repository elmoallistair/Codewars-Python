# Written: 20-Apr-2020
# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

def digital_root(n):
    temp = sum([int(i) for i in str(n)])

    if len(str(temp)) > 1:
        return digital_root(temp)
    else:
        return temp

    # if n >= 10:
    #     return digital_root(sum([int(i) for i in str(n)]))
    # else:
    #     return n
