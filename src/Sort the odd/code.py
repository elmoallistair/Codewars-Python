# Written: 21-Apr-2020
# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python

def sort_array(source_array):
    odd_arr = sorted([num for num in source_array if num%2 != 0])
    return [num if num%2 == 0 else odd_arr.pop(0) for num in source_array]
