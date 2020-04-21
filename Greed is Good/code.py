# Written: 21-Apr-2020
# https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python

def score(dice):
    points = 0
    for num in range(1, 7):
        val = dice.count(num)
        remainder = val%3
        if num == 1:
            points += (1000 if val >= 3 else 0) + (100 * remainder)
        else:
            points += 100 * num if val >= 3 else 0
            if num == 5:
                points += 50 * remainder
    return points
