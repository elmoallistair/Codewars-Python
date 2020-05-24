# Find The Parity Outlier

You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer `N`. 
Write a method that takes the array as an argument and returns this "outlier" `N`.

**Examples**

```
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
```

## Solution
```
def find_outlier(integers):
    is_odd = [x for x in integers if x%2!=0]
    is_even = [x for x in integers if x%2==0]
    return is_odd[0] if len(is_even) > 1 else is_even[0]
```

## Sample Tests
```
test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)
```
