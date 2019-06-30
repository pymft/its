# Polynomial

## Part 1

### main frame


```python
>>> # create a callable object for f(x) := x^2 + 2x + 3
>>> eq = Polynomial([1, 2, 3])
>>> # check degree
>>> eq.degree
2
>>> # check its coefficients
>>> eq.coefficients
(1, 2, 3)
>>> # and its value for x = 2 will be
>>> eq(2)   # 1 * 2 ** 2 + 2 * 2 ** 1 + 3 * 2 ** 
11
```

### solution 

```python 
class Polynomial:
    def __init__(self, coefficients):
        self.__coefficients = tuple(coefficients)
        self.__degree = len(coefficients) - 1 

    @property
    def coefficients(self):
        return self.__coefficients

    @property
    def degree(self):
        return self.__degree

    def __call__(self, x):
        value = 0
        for k, c in zip(range(self.degree, -1, -1), self.coefficients):
            value += c * x ** k
        return value
```

## Part2

### represent it
```python
>>> eq = Polynomial([8, 300, -2, 2, -3])
>>> eq
...    4      3    2    1    0
... +8x  +300x  -2x  +2x  -3x
```

### solution 

add `__repr__` method
```python
class Polynomial:
    # ...
    # Part 1
    # ...
    def __repr__(self):
        white_area = 2
        white_str = " " * white_area
        coef = list(map(lambda c: f"{c:+}x", self.coefficients))
        coef_whitespace = list(map(lambda c: " "*(len(c)-2), coef))
        pows = list(map(lambda i: f"{coef_whitespace[i]}{self.degree - i:2}", range(self.degree+1)))
        return " " + white_str.join(pows) + "\n" + white_str.join(coef)
```

## Part 3

### operators

```python
>>> f1 = Polynomial([1, 0, 1])
>>> f2 = Polynomial([1, 1, 2, 1])
>>> f3 = f2 - f1
>>> f3.coefficients
(1, 0, 2, 0,)
```

