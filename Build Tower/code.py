# Written: 20-Apr-2020
# https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python

def tower_builder(n_floors):
    return [('*'*(n*2-1)).center(n_floors*2-1) for n in range(1, n_floors+1)]
    # return [(' '*(n_floors-n-1) + '*'*(n*2+1) + ' '*(n_floors-n-1)) for n in range(n_floors)]
