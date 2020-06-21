# Written: 21-Jun-2020
# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

def find_it(seq):
    return [num for num in set(seq) if seq.count(num)%2][0]
