# Sort the Odd

# Instructions
You have an array of numbers.

Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example
```
sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
```

## Solution
```
def sort_array(source_array):
    odd_arr = sorted([num for num in source_array if num%2 != 0])
    return [num if num%2 == 0 else odd_arr.pop(0) for num in source_array]
```
