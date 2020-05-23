# Written: 23-May-2020
# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):
    return ' '.join([word if len(word) < 5 else word[::-1]for word in sentence.split()])
