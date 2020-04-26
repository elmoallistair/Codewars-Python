# Simple Pig Latin

## Instructions
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
```
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
```

## Solution
```
def pig_it(text):
    result = []
    for word in text.split():
        if word.isalpha():
            result.append(word[1:] + word[0] + 'ay' if len(word) > 1 else word + 'ay')
        else:
            result.append(word)

    return ' '.join(result)
```
```
def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())
```
