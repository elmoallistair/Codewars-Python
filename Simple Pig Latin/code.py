# Written: 20-Apr-2020
# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

def pig_it(text):
    result = []
    for word in text.split():
        if word.isalpha():
            result.append(word[1:] + word[0] + 'ay' if len(word) > 1 else word + 'ay')
        else:
            result.append(word)

    return ' '.join(result)
    
    # return ' '.join(word[1:] + word[0] + 'ay' if word.isalpha() else word for word in text.split())
