# Written: 27-Apr-2020
# https://www.codewars.com/kata/52223df9e8f98c7aa7000062/train/python

import codecs
import string

def rot13(message):
    # return codecs.encode(message, 'rot_13')

    ascii = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    rot13 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    return message.translate(message.maketrans(ascii, rot13))