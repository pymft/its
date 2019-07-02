class Polynomial:
    """ creates polynomial objects 
    
    >>> eq = Polynomial([1, 2, 3])
    >>> eq.degree
    2
    >>> eq.coefficients
    (1, 2, 3)
    >>> eq(2)
    11
    >>> Polynomial([8, 300, -2, 2, -3])
       4      3    2    1    0
    +8x  +300x  -2x  +2x  -3x
    """
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

    def __repr__(self):
        white_area = 2
        white_str = " " * white_area
        coef = list(map(lambda c: f"{c:+}x", self.coefficients))
        coef_whitespace = list(map(lambda c: " "*(len(c)-2), coef))
        pows = list(map(lambda i: f"{coef_whitespace[i]}{self.degree - i:2}", range(self.degree+1)))
        return " " + white_str.join(pows) + "\n" + white_str.join(coef)

if __name__ == '__main__':
    import doctest

    doctest.testmod()
