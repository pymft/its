# Simple Logger

## Part 1: logger decorator

keeps history of calls, arguments passed into decorated function and the result, all 
into a `*.csv` file

### usage

decorating `mysum()` function:

```python
@logme
def mysum(a, b):
    return a + b
```

try to call it multiple times, and out logfile will be updated. 
```
>>> mysum(1, 2)
3
>>> mysum(10, 20)
30
```

after calling `mysum` twice, we're going to 