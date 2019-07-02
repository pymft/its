# Simple Logger

## Part 1: logger decorator

keeps history of calls, arguments passed into decorated function and the result, all 
into a `*.csv` file

### usage

decorating `mysum()` function:

```python
import logme 


@logme.logme_part_one
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

after calling `mysum` twice, out `logs.csv` will look like this sample file:

```csv
"timestamp","function","args","kwargs,"returned_vals"
"1562093798.5783381","mysum","(1, 2,)","{}","3"
"1562093825.3916304","mysum","(10, 20,)","{}","30"
```

