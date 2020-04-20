# Written: 20-Apr-2020
# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python

def to_jaden_case(string):
    new_case = []
    for word in string.split():
        new_case.append(word.capitalize())
    return ' '.join(new_case)

    # return ' '.join([word.capitalize() for word in string.split()])
    # return ' '.join([word[0].upper() + word[1:] for word in string.split()])
