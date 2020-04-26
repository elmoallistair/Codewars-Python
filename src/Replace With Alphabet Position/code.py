# Written: 20-Apr-2020
# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

def alphabet_position(text):
    return ' '.join(str(ord(alph)-96) for alph in text.lower() if alph.isalpha())
