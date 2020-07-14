# Written: 14-Jul-2020
# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python

def high(x):
    score = []
    for word in x.split():
        score.append(sum([ord(letter)-96 for letter in word]))
    return x.split()[score.index(max(score))]
