class Polynomial:
    """ creates polynomial objects 
    
    >>> eq = Polynomial([1, 2, 3])
    >>> eq.degree
    2
    >>> eq.coefficients
    (1, 2, 3)
    >>> eq(2)
    11
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


if __name__ == '__main__':
    import doctest

    doctest.testmod()
