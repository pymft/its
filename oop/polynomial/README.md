# Polynomial

## Part 1

### objective 

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

