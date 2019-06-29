# Polynomial

![img](http://www.sciweavers.org/tex2img.php?eq=P%28x%29%20%3D%20a_%7Bn%7Dx%5E%7Bn%7D%2Ba_%7Bn-1%7Dx%5E%7Bn-1%7D%2B%5Cdotsb%20%2Ba_%7B2%7Dx%5E%7B2%7D%2Ba_%7B1%7Dx%2Ba_%7B0%7D%0A%0A%0A&bc=White&fc=Black&im=png&fs=18&ff=fourier&edit=0)

![img](http://www.sciweavers.org/tex2img.php?eq=P%28x%29%20%3D%20%7B%5Cdisplaystyle%20%5Csum%20_%7Bk%3D0%7D%5E%7Bn%7Da_%7Bk%7Dx%5E%7Bk%7D%7D%0A&bc=White&fc=Black&im=png&fs=18&ff=fourier&edit=0)

## Part 1

### main frame

![sample](http://www.sciweavers.org/tex2img.php?eq=P%28x%29%20%3D%201x%5E2%20%2B%202x%20%2B%203%0A%0A%0A%0A&bc=White&fc=Black&im=png&fs=12&ff=fourier&edit=0)

![values](http://www.sciweavers.org/tex2img.php?eq=P%282%29%20%3D%201%20%5Ctimes%20%202%20%5E%202%20%2B%202%20%5Ctimes%202%20%2B%203%20%3D%2011%0A%0A%0A%0A&bc=White&fc=Black&im=png&fs=12&ff=fourier&edit=0)

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

