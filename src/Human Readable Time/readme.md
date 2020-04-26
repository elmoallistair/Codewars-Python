# Human Readable Time
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (`HH:MM:SS`)
```
HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
```
The maximum time never exceeds 359999 (`99:59:59`)

You can find some examples in the test fixtures.

## Solution
```
def make_readable(second):
    mm, ss = divmod(second, 60) # mm = second // 60; ss = second % 60
    hh, mm = divmod(mm, 60)     # hh = mm // 60; mm = mm % 60
    return f'{hh:02d}:{mm:02d}:{ss:02d}'
```
```
def make_readable(second):
    return '{:02}:{:02}:{:02}'.format(second/3600, second/60%60, second%60)
```

## Sample Test
```
Test.assert_equals(make_readable(0), "00:00:00")
Test.assert_equals(make_readable(5), "00:00:05")
Test.assert_equals(make_readable(60), "00:01:00")
Test.assert_equals(make_readable(86399), "23:59:59")
Test.assert_equals(make_readable(359999), "99:59:59")
```