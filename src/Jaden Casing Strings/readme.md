# Jaden Casing Strings
Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

Example:
```
Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
```

## Solution
```
def to_jaden_case(string):
    new_case = []
    for word in string.split():
        new_case.append(word.capitalize())
    return ' '.join(new_case)
```
```
def to_jaden_case(string):
    return ' '.join([word.capitalize() for word in string.split()])
```
```
def to_jaden_case(string):
    return ' '.join([word[0].upper() + word[1:] for word in string.split()])
```

## Sample Test
```
quote = "How can mirrors be real if our eyes aren't real"
test.assert_equals(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")
```