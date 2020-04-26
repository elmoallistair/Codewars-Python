# Build Tower
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as `*`
* Python: return a `list`;
* JavaScript: returns an `Array`;
* C#: returns a `string[]`;
* PHP: returns an `array`;
* C++: returns a `vector<string>`;
* Haskell: returns a `[String]`;
* Ruby: returns an `Array`;

Have fun!

for example, a tower of 3 floors looks like below
```
[
  '  *  ', 
  ' *** ', 
  '*****'
]
```
and a tower of 6 floors looks like below
```
[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]
```

## Solution
```
def tower_builder(n_floors):
    return [('*'*(n*2-1)).center(n_floors*2-1) for n in range(1, n_floors+1)]
```
```
def tower_builder(n_floors):
    return [(' '*(n_floors-n-1) + '*'*(n*2+1) + ' '*(n_floors-n-1)) for n in range(n_floors)]
```

## Sample Test
```
test.describe("Tests")
test.it("Basic Tests")
test.assert_equals(tower_builder(1), ['*', ])
test.assert_equals(tower_builder(2), [' * ', '***'])
test.assert_equals(tower_builder(3), ['  *  ', ' *** ', '*****'])
```