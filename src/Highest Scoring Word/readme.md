# Highest Scoring Word

Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: `a = 1, b = 2, c = 3` etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

## Solution
```
def high(x):
    score = []
    for word in x.split():
        score.append(sum([ord(letter)-96 for letter in word]))
    return x.split()[score.index(max(score))]
```

## Sample Tests
```
test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
test.assert_equals(high('take me to semynak'), 'semynak')
```
