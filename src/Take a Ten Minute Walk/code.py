# Written: 20-Apr-2020
# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

def is_valid_walk(walk):
    return all([len(walk)==10, walk.count('n')==walk.count('s'), walk.count('e')==walk.count('w')])
