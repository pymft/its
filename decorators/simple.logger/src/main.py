import logme


@logme.logme_part_one
def mysum(a, b):
    return a + b


if __name__ == '__main__':
    mysum(1, 2)
    mysum(10, 20)