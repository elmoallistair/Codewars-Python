# Written: 20-Apr-2020
# https://www.codewars.com/kata/552c028c030765286c00007d/train/python

def iq_test(numbers):
    lst = ['even' if int(i)%2==0 else 'odd' for i in numbers.split()]
    if lst.count('even') > lst.count('odd'):
        return lst.index('odd')+1
    else:
        return lst.index('even')+1

    # lst = [int(i)%2==0 for i in numbers.split()]
    # return lst.index(False if lst.count(True)>lst.count(False) else True) + 1
