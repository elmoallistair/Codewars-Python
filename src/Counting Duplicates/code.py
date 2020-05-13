# Written 13-May-2020
# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

def duplicate_count(text):
    count = 0
    text = text.lower()
    for i in set(text):
        if text.count(i) > 1:
            count += 1
    return count
    # return len([i for i in set(text.lower()) if text.lower().count(i) > 1])
