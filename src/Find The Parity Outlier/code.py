# Written: 25-May-2020
# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/solutions/python

def find_outlier(integers):
    is_odd = [x for x in integers if x%2!=0]
    is_even = [x for x in integers if x%2==0]
    return is_odd[0] if len(is_even) > 1 else is_even[0]
