# IQ Test

## Instructions
Bob is preparing to pass IQ test. The most frequent task in this test is `to find out which one of the given numbers differs from the others`. 
Bob observed that one number usually differs from the others in evenness. 
Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

`!` Keep in mind that your task is to help Bob solve a real `IQ test`, which means indexes of the elements start from `1 (not 0)`

Examples :
```
iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
```

## Solution
```
def iq_test(numbers):
    lst = ['even' if int(i)%2==0 else 'odd' for i in numbers.split()]
    if lst.count('even') > lst.count('odd'):
        return lst.index('odd')+1
    else:
        return lst.index('even')+1
```
```
def iq_test(numbers):
    lst = [int(i)%2==0 for i in numbers.split()]
    return lst.index(False if lst.count(True)>lst.count(False) else True)+1
```

## Sample Test
```
Test.assert_equals(iq_test("2 4 7 8 10"),3)
Test.assert_equals(iq_test("1 2 2"), 1)
```