# Train: Square Every Digit

## Instruction
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 9<sup>2</sup> is 81 and 1<sup>2</sup> is 1.

**Note**: The function accepts an integer and returns an integer

## Solution
```
def square_digits(num):
    result = ''
    for i in str(num):
        result += str(int(i)**2)
    return int(result)
```
```
def square_digits(num):
    return int(''.join([str(int(i)**2) for i in str(num)]))
```
