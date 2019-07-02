import logme


@logme.logme_part_one
def mysum(a, b):
    return a + b

@logme.logme_part_two('logs_new.csv')
def mysub(a, b):
    return a - b

if __name__ == '__main__':
    mysub(9, 2)
    mysub(50, 20)