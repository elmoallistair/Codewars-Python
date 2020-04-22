# Written: 22-Apr-2020
# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

def make_readable(second):
    mm, ss = divmod(second, 60) # mm = second // 60; ss = second % 60
    hh, mm = divmod(mm, 60)     # hh = mm // 60; mm = mm % 60
    return f'{hh:02d}:{mm:02d}:{ss:02d}'
